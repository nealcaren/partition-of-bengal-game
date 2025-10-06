# Development Tasks: Bengal Partition Game Updates

## Overview
Please integrate the new opening vignette and add win/lose conditions to the game. The opening vignette data structure is saved in `opening_vignette.py`.

---

## Task 1: Integrate Multi-Page Opening Vignette

**Files to modify:** `server.py`, frontend HTML/JS

### Backend (server.py):
1. Import the vignette from `opening_vignette.py`
2. Replace the current `STARTING_SCENARIO` with the new multi-page structure
3. Create a new endpoint `/api/vignette` that returns the vignette pages sequentially or all at once (your choice)

### Frontend:
1. Display the vignette as a multi-page intro before gameplay starts
2. Show one page at a time with a "Continue" button (last page says "Begin Game")
3. Only start the actual game session after player clicks through all 4 pages
4. Store the session_id once created but don't send the first turn until vignette is complete

---

## Task 2: Remove Deprecated Stats

**Files to modify:** `server.py`

Remove these stats from the game entirely:
- `civil_liberties`
- `press_temperature`

Update in:
- `new_session_state()` function
- `SYSTEM_PROMPT` (remove mentions of these stats)
- Any other references in prompts or state management

---

## Task 3: Implement Win/Lose Conditions

**Files to modify:** `server.py`, frontend HTML/JS/CSS

### Win/Lose Rules:

**LOSE if:**
- `legitimacy < 20` OR
- `local_stability < 20` OR  
- `swadeshi_momentum > 85`

**WIN if:**
- Player survives until a set end date (suggest 1908-1911 timeframe, around 3-4 years game time)
- All stats remain in survivable ranges

### Backend Implementation (server.py):

1. **Add a check function** after each turn:
```python
def check_game_status(state: Dict[str, Any]) -> Dict[str, Any]:
    """Returns {'status': 'ongoing'|'victory'|'defeat', 'reason': str}"""
    if state['legitimacy'] < 20:
        return {'status': 'defeat', 'reason': 'legitimacy_collapse'}
    if state['local_stability'] < 20:
        return {'status': 'defeat', 'reason': 'stability_collapse'}
    if state['swadeshi_momentum'] > 85:
        return {'status': 'defeat', 'reason': 'swadeshi_unstoppable'}
    
    # Check if we've reached end date (convert date string to compare)
    # If date >= "1908-12-31" (or your chosen end date):
    #     return {'status': 'victory', 'reason': 'survived'}
    
    return {'status': 'ongoing', 'reason': ''}
```

2. **Call this function** in `/api/turn` after updating the state
3. **If game is over**, update the system prompt to tell the LLM to generate an appropriate ending narration based on the status/reason
4. **Return the game status** in the API response: `{"game_status": {...}, ...}`

### Frontend Implementation:

1. **Check for `game_status` field** in turn responses
2. **If game is over**, display the ending narration prominently and disable further input
3. **Show final stats** and outcome (Victory/Defeat + reason)
4. **Offer "Start New Game" button**

---

## Task 4: Add Visual Stat Warnings (CSS)

**Files to modify:** frontend CSS

Add visual indicators when stats are in danger zones:

### Danger Thresholds:
- `legitimacy` or `local_stability`: **Warning at <35, Critical at <25**
- `swadeshi_momentum`: **Warning at >70, Critical at >80**
- `reputation`: Just informational, no warnings needed

### CSS Requirements:
Create classes for stat display:
- `.stat-normal` - default/safe (white or light gray background)
- `.stat-warning` - approaching danger (yellow/orange background, maybe bold text)
- `.stat-critical` - near game over (red background, bold text, maybe pulse animation)

Apply these classes dynamically based on stat values.

### Suggested Visual Treatment:
```css
.stat-warning {
    background-color: #fff3cd;
    border-left: 4px solid #ffc107;
    font-weight: 600;
}

.stat-critical {
    background-color: #f8d7da;
    border-left: 4px solid #dc3545;
    font-weight: 700;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.7; }
}
```

---

## Testing Checklist

- [ ] Vignette displays all 4 pages in sequence
- [ ] Game doesn't start until "Begin Game" clicked
- [ ] Stats update correctly (only 4 stats remain)
- [ ] Game ends when legitimacy < 20
- [ ] Game ends when local_stability < 20  
- [ ] Game ends when swadeshi_momentum > 85
- [ ] Game ends with victory at end date
- [ ] Ending narration is appropriate to outcome
- [ ] Stat colors change at warning thresholds
- [ ] Stat colors change at critical thresholds
- [ ] "Start New Game" works after game over

---

## Questions?
Let me know if you need clarification on any of these tasks or want me to specify implementation details for any particular part.