#!/usr/bin/env python3
import uuid
from typing import Dict, Any, Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

from opening_vignette import OPENING_VIGNETTE
from story import (
    START_SCENE_ID,
    SCENES,
    apply_option,
    build_outcome_narration,
    build_scene_response,
    ensure_scene_date,
    find_option,
    parse_date,
)

GAME_VERSION = "v2.0.0"

app = FastAPI()



# ---- Lightweight in-memory session store (swap to Redis/DB for production) ----
SESSIONS: Dict[str, Dict[str, Any]] = {}

class TurnRequest(BaseModel):
    session_id: Optional[str] = None
    choice_id: Optional[str] = None

STATE_KEYS = ("date", "legitimacy", "local_stability", "swadeshi_momentum", "reputation", "version", "last_action")
END_DATE = "1908-12-31"
STATUS_MESSAGES = {
    "legitimacy_collapse": "Legitimacy has collapsed beneath acceptable levels; Bengal no longer trusts the Raj's word.",
    "stability_collapse": "Local unrest spirals beyond control; the machinery of governance breaks under the strain.",
    "swadeshi_unstoppable": "The swadeshi movement achieves unstoppable momentum, making the partition untenable.",
    "survived": "You navigated the turbulence through the end of 1908 without catastrophe, keeping imperial directives intact."
}

def new_session_state() -> Dict[str, Any]:
    start_date = SCENES.get(START_SCENE_ID, {}).get("date") or "1905-08-12"
    return {
        "date": start_date,
        "legitimacy": 60,
        "local_stability": 60,
        "swadeshi_momentum": 40,
        "reputation": 50,
        "log": [],
        "version": GAME_VERSION,
        "last_action": "",
        "scene_id": START_SCENE_ID,
        "flags": [],
        "history": [],
    }


def check_game_status(state: Dict[str, Any]) -> Dict[str, Any]:
    legitimacy = state.get("legitimacy")
    stability = state.get("local_stability")
    swadeshi = state.get("swadeshi_momentum")
    date_obj = parse_date(state.get("date"))

    if isinstance(legitimacy, (int, float)) and legitimacy < 20:
        return {"status": "defeat", "reason": "legitimacy_collapse", "message": STATUS_MESSAGES["legitimacy_collapse"]}
    if isinstance(stability, (int, float)) and stability < 20:
        return {"status": "defeat", "reason": "stability_collapse", "message": STATUS_MESSAGES["stability_collapse"]}
    if isinstance(swadeshi, (int, float)) and swadeshi > 85:
        return {"status": "defeat", "reason": "swadeshi_unstoppable", "message": STATUS_MESSAGES["swadeshi_unstoppable"]}

    end_date_obj = parse_date(END_DATE)
    if date_obj and end_date_obj and date_obj >= end_date_obj:
        return {"status": "victory", "reason": "survived", "message": STATUS_MESSAGES["survived"]}

    return {"status": "ongoing", "reason": "", "message": ""}

@app.post("/api/turn")
def turn(req: TurnRequest):
    # Make/get session
    sid = req.session_id or str(uuid.uuid4())
    if sid not in SESSIONS:
        SESSIONS[sid] = new_session_state()

    state = SESSIONS[sid]
    already_over = state.get("game_status", {}).get("status") in {"victory", "defeat"}
    if already_over:
        data = build_scene_response(state.get("scene_id", START_SCENE_ID), state)
        data["options"] = []
        reason = state.get("game_status", {}).get("reason", "")
        data["narration"] = (data.get("narration", "") + "\n\n" + build_outcome_narration(reason)).strip()
    else:
        choice_id = (req.choice_id or "").strip()
        if choice_id:
            option = find_option(state.get("scene_id", START_SCENE_ID), choice_id, state)
            if not option:
                raise HTTPException(status_code=400, detail="Unknown option for current scene.")
            apply_option(state, option)
            state["last_action"] = choice_id
            state["history"].append(choice_id)
            state["scene_id"] = option.get("next", START_SCENE_ID)
        ensure_scene_date(state, state.get("scene_id", START_SCENE_ID))
        data = build_scene_response(state.get("scene_id", START_SCENE_ID), state)

    if data.get("narration"):
        state["log"].append(data["narration"])

    status_info = check_game_status(state)
    state["game_status"] = status_info

    if status_info["status"] != "ongoing" and not already_over:
        outcome = build_outcome_narration(status_info["reason"])
        if outcome:
            data["narration"] = (data.get("narration", "") + "\n\n" + outcome).strip()
        data["options"] = []

    sanitized_state = {key: state.get(key) for key in STATE_KEYS}
    data["state"] = sanitized_state
    data["game_status"] = status_info

    return JSONResponse({"session_id": sid, **data})

@app.get("/api/new")
def new():
    sid = str(uuid.uuid4())
    SESSIONS[sid] = new_session_state()
    return {"session_id": sid, "message": "New session created."}

@app.get("/api/vignette")
def vignette():
    return OPENING_VIGNETTE

# Serve the static frontend (index.html)
app.mount("/", StaticFiles(directory="static", html=True), name="static")
