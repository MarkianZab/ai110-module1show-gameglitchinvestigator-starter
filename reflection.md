# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

1. **Lying hints.** Expected: guessing too high tells me to go lower. Actual: it told me to "Go HIGHER" when I was already too high.

2. **Impossible to win.** Expected: guessing the secret wins. Actual: on even attempts the secret was compared as a string, so a correct guess never registered as a win.

3. **Wrong attempt count.** Expected: a fresh game shows the full number of attempts. Actual: the counter started at 1, so it showed one fewer than it should.

### Bug Reproduction Logs

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output |
|---|---|---|---|
| guess 80, secret 50 | hint "Go LOWER" | hint "Go HIGHER" | none |
| correct guess on 2nd attempt | win | no win registered | TypeError (str vs int) |
| open app, before guessing (Normal) | "Attempts left: 8" | "Attempts left: 7" | none |

## 2. How did you use AI as a teammate?

I used Claude to help diagnose and fix the bugs.

Correct suggestion: Claude spotted that `check_guess` had inverted hints — a too-high guess told the player to "Go HIGHER." It suggested swapping them. I verified in the live app (80 vs secret 50 now says "Go LOWER") and with a pytest case checking the hint contains "LOWER."

Incorrect/misleading suggestion: The starter tests expected `check_guess` to return a string, but it returns a tuple `(outcome, message)`. Trusting them would have meant breaking the function. I caught it and fixed the tests to read `result[0]`, then confirmed all tests pass.

## 3. Debugging and testing your fixes

I verified each fix two ways: by playing the live app (with the Developer Debug Info expander open to see the secret) and by running pytest. After fixing the hint logic, guessing too high now correctly says "Go LOWER." After removing the string cast, a correct guess wins on any attempt. I wrote/corrected four pytest cases in tests/test_game_logic.py covering win, too-high, too-low, and a check that the too-high hint contains "LOWER" — all four pass (see test_results.txt).

## 4. What did you learn about Streamlit and state?

Streamlit re-runs the whole script top to bottom on every interaction, so normal variables reset each time. `st.session_state` persists across reruns, so things that must survive — the secret, score, attempts — live there. That's exactly why the secret had to be stored in session state: otherwise it re-rolled on every guess and the game was impossible to win.

## 5. Looking ahead: your developer habits

**Habit to reuse:** Running `pytest` to verify every fix instead of assuming it worked — it's how I caught a test asserting the wrong return type.

**Do differently with AI:** Read the actual output and diff before trusting it. The AI looked confident even when its suggestion didn't match my real code.

**How my thinking changed:** I now treat AI-generated code as a draft to verify, not an answer to trust. Whether the code is correct is on me, not the tool.