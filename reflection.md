# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

1. **Lying hints.** Expected: guessing too high tells me to go lower. Actual:
   it told me to "Go HIGHER" when I was already too high.
2. **Impossible to win.** Expected: guessing the secret wins. Actual: on even
   attempts the secret was compared as a string, so a correct guess never
   registered as a win.
3. **Wrong attempt count.** Expected: a fresh game shows the full number of
   attempts. Actual: the counter started at 1, so it showed one fewer than it should.

### Bug Reproduction Logs

| Input Used | Expected Behavior | Actual Behavior | Console Error / Output |
|---|---|---|---|
| guess 80, secret 50 | hint "Go LOWER" | hint "Go HIGHER" | none |
| correct guess on 2nd attempt | win | no win registered | TypeError (str vs int) |
| open app, before guessing (Normal) | "Attempts left: 8" | "Attempts left: 7" | none |

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

I verified each fix two ways: by playing the live app (with the Developer Debug
Info expander open to see the secret) and by running pytest. After fixing the
hint logic, guessing too high now correctly says "Go LOWER." After removing the
string cast, a correct guess wins on any attempt. I wrote/corrected four pytest
cases in tests/test_game_logic.py covering win, too-high, too-low, and a check
that the too-high hint contains "LOWER" — all four pass (see test_results.txt).

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
