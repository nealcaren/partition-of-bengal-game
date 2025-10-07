#!/usr/bin/env python3
import os, uuid, json
from datetime import datetime, timedelta
from typing import Dict, Any, List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

# ---- LLM client (OpenAI-compatible) ----
# pip install openai fastapi uvicorn pydantic
from openai import OpenAI

from opening_vignette import OPENING_VIGNETTE, STARTING_SCENARIO

GAME_VERSION = "v1.2.0"

#client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
client = OpenAI(
    api_key=os.environ.get("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

app = FastAPI()



# ---- Lightweight in-memory session store (swap to Redis/DB for production) ----
SESSIONS: Dict[str, Dict[str, Any]] = {}

# ---- Prompt “content pack” to ground the game ----
HISTORICAL_FACTS = """
Partition of Bengal (1905) split the 78-million-person Bengal Presidency into Eastern Bengal & Assam (capital Dacca) and a reduced Western Bengal joined with Bihar and Orissa (capital Calcutta).
British officials framed the move as administrative efficiency after decades of complaints that the unwieldy province neglected the east; Bengali Hindus (bhadralok) saw it as divide and rule that reduced Bengali speakers to a minority in the west.
Hindu revivalists such as Bal Tilak, V. D. Savarkar, and Bipin Chandra Pal championed swadeshi boycotts, bonfires of British cloth, and in some cases conspiratorial violence (e.g., the Alipore bomb plot against Magistrate Kingsford). Moderates like Surendranath Banerjee and Gopal Krishna Gokhale organised petitions and legal protest via papers such as *The Bengalee*.
Muslim elites, influenced by Syed Ahmad Khan’s appeals to loyalism, welcomed Curzon’s promise of a Muslim-majority province; Nawab Salimullah of Dacca led support for the partition and later helped found the All-India Muslim League in 1906. The Raj introduced separate electorates for Muslims, deepening Congress resentment.
Key flashpoints: Section 144 restrictions on gatherings, Vernacular Press Act censorship, sedition prosecutions (Tilak), swadeshi pickets in Calcutta College Square and Howrah, unrest spreading to Poona, assassinations and attempted assassinations (e.g., 1908 Muzaffarpur bombing).
Outcomes: Intensified Hindu-Muslim political divergence; administrative reunification in 1911 accompanied by moving the imperial capital to Delhi; revolutionary nationalism and communal politics both accelerated.
Use period language with care; avoid anachronism; keep neutral instructional tone while roleplaying officials’ briefs.
"""

TIMELINE_EVENTS = [
    {
        "id": "partition_proclaimed",
        "date": "1905-10-16",
        "instruction": "Narrate the formal proclamation bringing Bengal partition into effect and the immediate reactions in Calcutta and Dacca.",
        "summary": "[Timeline • 16 Oct 1905] The Raj proclaims Bengal officially divided; Calcutta erupts in protest while Dacca’s loyalists celebrate the new province."
    },
    {
        "id": "muslim_league_formed",
        "date": "1906-12-30",
        "instruction": "Describe the Dacca meeting at Ahsan Manzil where Nawab Salimullah and allies launch the All-India Muslim League and outline its loyalist aims.",
        "summary": "[Timeline • 30 Dec 1906] At Ahsan Manzil, Nawab Salimullah hosts delegates who found the All-India Muslim League, pledging Muslim loyalty to the Raj."
    },
    {
        "id": "kingsford_bomb",
        "date": "1908-04-30",
        "instruction": "Report the Muzaffarpur bombing targeting Magistrate Kingsford, noting the civilian casualties and ensuing police crackdown.",
        "summary": "[Timeline • 30 Apr 1908] Revolutionaries hurl a bomb at Magistrate Kingsford’s carriage in Muzaffarpur, killing two British women and triggering sweeping arrests."
    },
    {
        "id": "tilak_sedition",
        "date": "1908-07-22",
        "instruction": "Cover Bal Tilak’s sedition conviction and transportation sentence, including how moderates and radicals respond.",
        "summary": "[Timeline • 22 Jul 1908] A Bombay court convicts Bal Tilak of sedition and orders transportation; moderates urge calm while radicals hail him as martyr."    
    }
]

SYSTEM_PROMPT = f"""
You are the Game Master for an educational, historically grounded interactive fiction.
SETTING: British India, 1905–1908 (Partition of Bengal & Swadeshi Movement).
PLAYER ROLE: Viceroy's aide (private secretary/administrative advisor).

REQUIREMENTS:
- Be accurate and cite period names, policies, and factions naturally in narration (no URLs, no modern citations).
- Keep turns concise: ~150–250 words + clear options.
- Maintain game STATE as JSON you return each turn (append at the end under 'state'), including stats and current date.
- After each player input, update: legitimacy, local_stability, swadeshi_momentum, reputation.
- Advance the calendar by roughly 3–6 weeks each turn (never less than 14 days) unless a timeline event explicitly demands a shorter window.
- Offer 3–5 actionable choices, each with short rationale.
- Include a 1-2 sentence teaching note each turn highlighting key takeaways.
- Emphasize contrasts between Hindu moderates and radicals, British divide-and-rule tactics, and Muslim League loyalism when relevant.

SAFETY & PEDAGOGY:
- Do not generate hate speech or endorse ethnic/religious hatred.
- Use neutral framing for communal tensions; emphasize complexity.
- Contextualize violence (bombings, assassinations, executions) without glamorizing; acknowledge competing contemporary views.
- If the player requests purely punitive or incendiary actions, warn about historical consequences and provide tempered alternatives.

HISTORICAL FACTS YOU MUST RESPECT:
{HISTORICAL_FACTS}
"""

class TurnRequest(BaseModel):
    session_id: Optional[str] = None
    user_input: Optional[str] = ""

STATE_KEYS = ("date", "legitimacy", "local_stability", "swadeshi_momentum", "reputation", "version", "last_action")
END_DATE = "1908-12-31"
STATUS_MESSAGES = {
    "legitimacy_collapse": "Legitimacy has collapsed beneath acceptable levels; Bengal no longer trusts the Raj's word.",
    "stability_collapse": "Local unrest spirals beyond control; the machinery of governance breaks under the strain.",
    "swadeshi_unstoppable": "The swadeshi movement achieves unstoppable momentum, making the partition untenable.",
    "survived": "You navigated the turbulence through the end of 1908 without catastrophe, keeping imperial directives intact."
}

def new_session_state() -> Dict[str, Any]:
    return {
        "date": "1905-08-15",
        "legitimacy": 60,
        "local_stability": 60,
        "swadeshi_momentum": 40,
        "reputation": 50,
        "log": [],
        "events_triggered": [],
        "version": GAME_VERSION,
        "last_action": ""
    }

def game_messages(state: Dict[str, Any], user_input: str) -> List[Dict[str, str]]:
    # We include a compressed state so the model remains consistent
    compact_state = {k: state[k] for k in state if k not in {"log", "game_status"}}
    state_summary = json.dumps(compact_state)[:2000]
    history_clip = "\n".join(state.get("log", [])[-6:])  # last few turns
    due_events = get_due_events(state)
    action_context = (user_input.strip() or state.get("last_action") or "standing directives from the Secretariat")
    timeline_instructions = "\n".join(
        f"- Regardless of the directive \"{action_context}\", {event['instruction']} Explain how this development complicates that choice and present updated options." 
        for event in due_events
    )
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

Ensure exactly one option invites the player to gather information (e.g., interview a figure, request a report, conduct reconnaissance) so the learner can explore context before acting without overwhelming the choice set.

Victory and defeat thresholds:
- Defeat if legitimacy < 20, local_stability < 20, or swadeshi_momentum > 85.
- Victory if the date reaches or exceeds {END_DATE} while avoiding those defeats.

If the game ends, set "game_status" to {{"status": "victory"|"defeat", "reason": one of legitimacy_collapse, stability_collapse, swadeshi_unstoppable, survived}} and craft an ending narration acknowledging the outcome.

Anchor narration to the textbook emphasis: highlight tensions between Congress moderates and Hindu radicals, explain how swadeshi tactics escalate, note Muslim League loyalism and British divide-and-rule strategy when appropriate, and define unfamiliar terms or figures succinctly (e.g., Bhadralok, Nawab Salimullah, Magistrate Kingsford, Alipore plot) when they appear.

Advance the in-world date by roughly 3–6 weeks per turn (never less than 14 days) unless a timeline event requires a precise day; note the new date explicitly in the state.

Keep numbers in 0–100. Advance date realistically (days/weeks).
Never include URLs. Avoid modern slang. Keep tone immersive but instructional.
"""
    if timeline_instructions:
        developer_prompt += f"\nMandatory timeline events this turn:\n{timeline_instructions}\n"
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


def get_due_events(state: Dict[str, Any]) -> List[Dict[str, str]]:
    current_date = parse_date(state.get("date"))
    if not current_date:
        return []
    triggered = set(state.get("events_triggered") or [])
    due: List[Dict[str, str]] = []
    for event in TIMELINE_EVENTS:
        event_date = parse_date(event["date"])
        if event_date and current_date >= event_date and event["id"] not in triggered:
            due.append(event)
    return due


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
    previous_date = parse_date(state.get("date"))

    # Call LLM
    try:
        resp = client.chat.completions.create(
            model="gemini-2.5-flash",  # or your preferred chat model
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
        # Ensure date advances meaningfully
        current_date = parse_date(SESSIONS[sid].get("date"))
        if previous_date and (not current_date or current_date <= previous_date):
            adjusted = previous_date + timedelta(days=21)
            SESSIONS[sid]["date"] = adjusted.strftime("%Y-%m-%d")
        # Append narration to log
        if "narration" in data:
            SESSIONS[sid]["log"].append(data["narration"])
        if "events_triggered" not in SESSIONS[sid]:
            SESSIONS[sid]["events_triggered"] = []
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Bad model JSON: {e}")

    due_events_post = get_due_events(SESSIONS[sid])
    if due_events_post:
        additions = []
        for event in due_events_post:
            additions.append(event["summary"])
            SESSIONS[sid]["events_triggered"].append(event["id"])
        extra_text = "\n\n".join(additions)
        existing_narration = data.get("narration", "")
        combined = (existing_narration + ("\n\n" if existing_narration and extra_text else "") + extra_text).strip()
        data["narration"] = combined
        if SESSIONS[sid]["log"]:
            SESSIONS[sid]["log"][-1] = combined
        else:
            SESSIONS[sid]["log"].append(combined)

    SESSIONS[sid]["last_action"] = user_input.strip()

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
