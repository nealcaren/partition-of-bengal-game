# Divide and Rule: The Bengal Partition Crisis of 1905

A browser-based, LLM-driven strategy narrative set during the run-up to the 1905 Partition of Bengal. You serve as the Viceroy’s private secretary, steering policy, holding the line against unrest, and deciding when to conciliate or coerce. Each turn acts like a dispatch cycle: you select a course of action, an AI Game Master updates the situation, and the province’s political climate shifts accordingly.

---

## Gameplay Highlights

- **Multi-page prologue** drawn from archival context sets up the stakes before play begins.
- **Dynamic narration** from the LLM reacts to your directives with historically grounded consequences.
- **Four core stats** — Legitimacy, Local Stability, Swadeshi Momentum, Reputation — track your standing and display real-time warning colours plus trend arrows for every change.
- **Period telegraph overlay** appears whenever a decision is en route to the Game Master, keeping the board readable while you wait.
- **Persistence-free sessions** backed by an in-memory store; perfect for rapid iteration and classroom demos.

---

## Win / Lose Conditions

You are dismissed immediately if any one of these thresholds is crossed:

- **Legitimacy < 20** – Calcutta and London no longer trust your assurances.
- **Local Stability < 20** – Riots, strikes, and violence overwhelm the administration.
- **Swadeshi Momentum > 85** – The boycott movement becomes unstoppable.

Survive unchanged through **31 December 1908** (the canonical end-date for the scenario) and you win by outlasting the crisis. Reputation influences optics and narrative tone but will not end the game on its own.

---

## Tech Stack

| Layer      | Details                                                    |
|------------|------------------------------------------------------------|
| Backend    | Python 3.10+, FastAPI, Uvicorn                             |
| LLM Client | OpenAI-compatible `chat.completions` API                   |
| Frontend   | Static HTML, modern CSS, vanilla ES modules-free JavaScript|
| Data       | In-memory session store (easy to swap for Redis later)     |

---

## Getting Started

1. **Install dependencies**
   ```bash
   pip install fastapi uvicorn openai pydantic
   ```

2. **Set your OpenAI-compatible API key**
   ```bash
   export OPENAI_API_KEY="sk-..."
   ```

3. **Run the server**
   ```bash
   uvicorn server:app --reload
   ```

4. **Open the client**
   Visit `http://127.0.0.1:8000/` in your browser. The static frontend is served directly by FastAPI, so no extra build step is needed.

---

## Development Notes

- **Opening vignette**: Served from `/api/vignette`, then rendered one page at a time before the game session starts.
- **Game loop**: `/api/turn` expects `{ session_id, user_input }` and returns narration, updated state, and (when relevant) a `game_status` payload.
- **Sessions**: `/api/new` seeds a fresh state; the current implementation stores everything in the `SESSIONS` dict.
- **Frontend enhancements**: stat tiles add colour-coded severity, plus ▲/▼ arrows that reflect whether the change helps or harms you (momentum drops are celebrated, spikes are flagged red).

---

## Testing & Diagnostics

- Quick syntax check: `python -m compileall server.py opening_vignette.py`
- Manual play-through remains the primary validation loop; consider integrating recorded transcripts or snapshot tests once the narrative settles.

---

## Roadmap Ideas

- Persist sessions in Redis/Postgres for multi-player classrooms.
- Add optional “advisor briefs” that summarise consequences of past turns.
- Extend the timeline beyond 1908 or branch into post-annulment scenarios.
- Offer accessibility toggles (reduced motion already supported via CSS, but more can be added).

Contributions welcome! Open an issue or submit a PR if you build new historical events, balancing tweaks, or teaching aids.
