# Divide and Rule: The Bengal Partition Crisis of 1905

A browser-based, scripted strategy narrative set during the run-up to the 1905 Partition of Bengal. You serve as the Viceroy’s private secretary, steering policy, holding the line against unrest, and deciding when to conciliate or coerce. Each turn acts like a dispatch cycle: you select a course of action, the scenario engine advances the timeline, and the province’s political climate shifts accordingly.

---

## Gameplay Highlights

- **Multi-page prologue** drawn from archival context sets up the stakes before play begins.
- **Rapid play** through fixed, historically grounded decision branches (3–4 options per turn).
- **Four core stats** — Legitimacy, Local Stability, Swadeshi Momentum, Reputation — track your standing and display real-time warning colours plus trend arrows for every change.
- **Period telegraph overlay** appears whenever a decision is en route to the Game Master, keeping the board readable while you wait.
- **Persistence-free sessions** backed by an in-memory store; perfect for rapid iteration and classroom demos.

---

## Win / Lose Conditions

You are dismissed immediately if any one of these thresholds is crossed:

- **Legitimacy collapses** (score under 20) – Calcutta and London no longer trust your assurances.
- **Local Stability collapses** (score under 20) – Riots, strikes, and violence overwhelm the administration.
- **Swadeshi Momentum becomes unstoppable** (score above 85) – The boycott movement can no longer be contained.

Survive unchanged through **31 December 1908** (the canonical end-date for the scenario) and you win by outlasting the crisis. Reputation influences optics and narrative tone but will not end the game on its own.

---

## Tech Stack

| Layer      | Details                                                    |
|------------|------------------------------------------------------------|
| Engine     | Scripted scenario graph (fixed branches + stat effects)    |
| Frontend   | Static HTML, modern CSS, vanilla ES modules-free JavaScript|
| Hosting    | Static (GitHub/Google Pages)                               |

---

## Getting Started

### Static Hosting

- Host the contents of `static/` on GitHub Pages, Google Pages, or any static host.
- Point your host to `static/index.html` as the entry point.

### Local Development

1. **Open the client**
   Open `static/index.html` in your browser.

---

## Development Notes

- **Opening vignette**: Stored in `static/content.js` and rendered one page at a time before play begins.
- **Scenario graph**: Core narrative branches and stat effects live in `static/content.js`.
- **Game loop**: Runs entirely in-browser; each choice advances the state immediately.
- **Frontend enhancements**: stat tiles add colour-coded severity, plus ▲/▼ arrows that reflect whether the change helps or harms you (momentum drops are celebrated, spikes are flagged red).

---

## Testing & Diagnostics

- Open `static/index.html` directly or via any static host and play through a full run.
- Manual play-through remains the primary validation loop; consider integrating recorded transcripts or snapshot tests once the narrative settles.

---

## Roadmap Ideas

- Persist sessions in Redis/Postgres for multi-player classrooms.
- Add optional “advisor briefs” that summarise consequences of past turns.
- Extend the timeline beyond 1908 or branch into post-annulment scenarios.
- Offer accessibility toggles (reduced motion already supported via CSS, but more can be added).

Contributions welcome! Open an issue or submit a PR if you build new historical events, balancing tweaks, or teaching aids.