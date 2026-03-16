# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

When I first ran the game, it looked like a normal Streamlit guessing game with a sidebar for difficulty settings and a text input for guesses. However, once I started playing, things fell apart quickly. The Developer Debug Info panel showed the secret number, which made it easy to confirm the bugs I was seeing.

- **Bug 1 — Reversed hints:** When I guessed 50 and the secret was 29, the game told me to "Go HIGHER!" instead of "Go LOWER!" The hint messages in `check_guess()` were swapped — `guess > secret` returned "Go HIGHER!" when it should have said "Go LOWER!", and vice versa.
- **Bug 2 — Hard mode is actually easier than Normal:** The difficulty range for "Hard" was set to 1–50, while "Normal" was 1–100. This means Hard mode gives you a smaller range to guess from, which is the opposite of what you'd expect — Hard should be harder, not easier.
- **Bug 3 — Secret number changes type on even attempts:** On every even-numbered attempt, the code converts the secret number to a string before comparing it to the guess. This causes the comparison to break because you're comparing an integer to a string, leading to unpredictable hint behavior.
- **Bug 4 — Score changes erratically:** The `update_score()` function adds 5 points for a "Too High" guess on even attempts but subtracts 5 on odd attempts. "Too Low" always subtracts 5. This makes the score swing wildly depending on which attempt number you're on, which makes no sense from a gameplay perspective.
- **Bug 5 — Attempts counter starts at 1 instead of 0:** The attempts counter initializes to 1, which means you effectively lose one attempt before you even play. Combined with the display showing `attempt_limit - attempts`, the "Attempts left" number is off by one from the start.

---

## 2. How did you use AI as a teammate?

I used VS Code Copilot (Chat and Agent modes) to help investigate and fix the game. I shared the full codebase context using `#file:app.py` and `#file:logic_utils.py` so the AI could see how the UI and logic files related to each other.

- **Correct suggestion:** When I described the reversed hints bug, Copilot correctly identified that the messages in `check_guess()` were swapped — `guess > secret` was returning "Go HIGHER!" instead of "Go LOWER!". I verified this by checking the debug panel (secret was 29), guessing 50, and confirming that after the fix the hint correctly said "Go LOWER!".
- **Incorrect/misleading suggestion:** When I asked Copilot to fix the scoring, it initially suggested removing the penalty entirely for wrong guesses, arguing that "negative scores are unfriendly." However, that would have removed the incentive to guess efficiently. I rejected this and instead made the deduction a consistent -5 for every wrong guess regardless of attempt number, which keeps the scoring fair and predictable.

---

## 3. Debugging and testing your fixes

I used a combination of manual testing and automated pytest to confirm each fix. For manual testing, I would run `streamlit run app.py`, open the Developer Debug Info panel to see the secret number, and then make guesses that I knew should be higher or lower to verify the hints were correct.

For automated testing, I wrote pytest cases in `tests/test_game_logic.py`. For example, `test_hint_message_when_too_high` calls `check_guess(60, 50)` and asserts that the message contains "LOWER" — this directly targets the reversed-hints bug. I also wrote `test_score_deduction_is_consistent` which checks that `update_score(100, "Too High", 2)` and `update_score(100, "Too High", 3)` both return 95, confirming the scoring no longer depends on attempt parity. All 9 tests pass cleanly.

Copilot helped me think about what to test by suggesting edge-case scenarios. When I asked it to generate tests, it proposed checking both the outcome string and the hint message text separately, which was a good pattern — it let me verify both the game logic and the user-facing feedback in the same test file.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
