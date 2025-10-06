#!/usr/bin/env python3
import os, uuid, json
from datetime import datetime
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

# ---- LLM client (OpenAI-compatible) ----
# pip install openai fastapi uvicorn pydantic
from openai import OpenAI

from opening_vignette import OPENING_VIGNETTE, STARTING_SCENARIO

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

app = FastAPI()



# ---- Lightweight in-memory session store (swap to Redis/DB for production) ----
SESSIONS: Dict[str, Dict[str, Any]] = {}

# ---- Prompt “content pack” to ground the game ----
HISTORICAL_FACTS = """
Partition of Bengal (1905) split Bengal into Eastern Bengal & Assam (capital Dacca) and a reduced Bengal (capital Calcutta).
British rationale: administrative efficiency; Indian criticism: divide-and-rule, communal/linguistic split.
Key figures & strands: Curzon; Minto; Indian National Congress moderates (Surendranath Banerjee, Gokhale); extremist leaders (Bipin Chandra Pal, Aurobindo Ghose, Lajpat Rai); Rabindranath Tagore.
Swadeshi Movement: boycott of British goods; promotion of indigenous industry (khadi, handlooms); picketing; bonfires of foreign cloth; national education initiatives.
Key issues: press controls (vernacular press), Section 144 orders, sedition charges, deportations without trial, police lathi charges, student strikes.
Outcomes: Deepened anti-colonial mobilization; partition **annulled in 1911**, capital moved to Delhi.
Use period language with care; avoid anachronism; keep neutral instructional tone while roleplaying officials’ briefs.
"""

SYSTEM_PROMPT = f"""
You are the Game Master for an educational, historically grounded interactive fiction.
SETTING: British India, 1905–1908 (Partition of Bengal & Swadeshi Movement).
PLAYER ROLE: Viceroy's aide (private secretary/administrative advisor).

REQUIREMENTS:
- Be accurate and cite period names, policies, and factions naturally in narration (no URLs, no modern citations).
- Keep turns concise: ~150–250 words + clear options.
- Maintain game STATE as JSON you return each turn (append at the end under 'state'), including stats and current date.
- After each player input, update: legitimacy, local_stability, swadeshi_momentum, reputation.
- Advance time sensibly (days/weeks).
- Offer 3–5 actionable choices, each with short rationale.

SAFETY & PEDAGOGY:
- Do not generate hate speech or endorse ethnic/religious hatred.
- Use neutral framing for communal tensions; emphasize complexity.
- If the player requests purely punitive or incendiary actions, warn about historical consequences and provide tempered alternatives.

HISTORICAL FACTS YOU MUST RESPECT:
{HISTORICAL_FACTS}
"""

class TurnRequest(BaseModel):
    session_id: Optional[str] = None
    user_input: Optional[str] = ""

STATE_KEYS = ("date", "legitimacy", "local_stability", "swadeshi_momentum", "reputation")
END_DATE = "1908-12-31"
STATUS_MESSAGES = {
    "legitimacy_collapse": "Legitimacy has collapsed beneath acceptable levels; Bengal no longer trusts the Raj's word.",
    "stability_collapse": "Local unrest spirals beyond control; the machinery of governance breaks under the strain.",
    "swadeshi_unstoppable": "The swadeshi movement achieves unstoppable momentum, making the partition untenable.",
    "survived": "You navigated the turbulence through the end of 1908 without catastrophe, keeping imperial directives intact."
}

def new_session_state() -> Dict[str, Any]:
    return {
        "date": "1905-07-15",
        "legitimacy": 60,
        "local_stability": 60,
        "swadeshi_momentum": 40,
        "reputation": 50,
        "log": []
    }

def game_messages(state: Dict[str, Any], user_input: str) -> List[Dict[str, str]]:
    # We include a compressed state so the model remains consistent
    compact_state = {k: state[k] for k in state if k not in {"log", "game_status"}}
    state_summary = json.dumps(compact_state)[:2000]
    history_clip = "\n".join(state.get("log", [])[-6:])  # last few turns
    developer_prompt = f"""
You are continuing an educational game. Current compact state:
{state_summary}

Recent log:
{history_clip}

If user_input is empty, start the game with the starting scenario provided.
Always return a JSON object with keys:
- "narration": rich 150–250 word scene update (period-appropriate),
- "options": array of 3–5 concise strings the player can choose or type,
- "learned": short teaching note (1–2 sentences),
- "state": updated game state dict (date, legitimacy, local_stability, swadeshi_momentum, reputation),
- optional "game_status" when the campaign ends.

Victory and defeat thresholds:
- Defeat if legitimacy < 20, local_stability < 20, or swadeshi_momentum > 85.
- Victory if the date reaches or exceeds {END_DATE} while avoiding those defeats.

If the game ends, set "game_status" to {{"status": "victory"|"defeat", "reason": one of legitimacy_collapse, stability_collapse, swadeshi_unstoppable, survived}} and craft an ending narration acknowledging the outcome.

Keep numbers in 0–100. Advance date realistically (days/weeks).
Never include URLs. Avoid modern slang. Keep tone immersive but instructional.
"""
    msgs = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"STARTING_SCENARIO:\n{STARTING_SCENARIO}"},
        {"role": "user", "content": f"USER_INPUT:\n{user_input.strip() or '[START]'}"},
        {"role": "developer", "content": developer_prompt}
    ]
    return msgs


def parse_date(date_str: Optional[str]):
    if not date_str:
        return None
    try:
        return datetime.strptime(str(date_str), "%Y-%m-%d").date()
    except ValueError:
        return None


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
    user_input = (req.user_input or "").strip()

    # Call LLM
    try:
        resp = client.chat.completions.create(
            model="gpt-5-mini",  # or your preferred chat model
            temperature=1,
            messages=game_messages(state, user_input),
            response_format={"type": "json_object"},
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    # Parse model JSON
    try:
        content = resp.choices[0].message.content
        data = json.loads(content)
        # Update session state + log
        if "state" in data and isinstance(data["state"], dict):
            for key in STATE_KEYS:
                if key in data["state"]:
                    SESSIONS[sid][key] = data["state"][key]
        # Append narration to log
        if "narration" in data:
            SESSIONS[sid]["log"].append(data["narration"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Bad model JSON: {e}")

    status_info = check_game_status(SESSIONS[sid])
    SESSIONS[sid]["game_status"] = status_info

    sanitized_state = {key: SESSIONS[sid][key] for key in STATE_KEYS}
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
