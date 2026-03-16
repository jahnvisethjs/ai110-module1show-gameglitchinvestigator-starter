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

Streamlit works differently from a normal Python script — every time you interact with the app (click a button, type in an input), the entire script re-runs from top to bottom. This means that if you store a variable the normal way (like `secret = 42`), it gets reset to its initial value on every interaction. To fix this, Streamlit provides `st.session_state`, which acts like a persistent dictionary that survives between reruns. So `st.session_state.secret` keeps its value even when the page re-runs after you click "Submit Guess." This was critical for this project because the secret number, score, and attempt count all need to persist across interactions — without session state, every guess would reset the game.

---

## 5. Looking ahead: your developer habits

- **One habit I want to reuse:** Writing targeted pytest cases immediately after fixing a bug. It forced me to think clearly about what "fixed" actually means — not just "it doesn't crash," but "given this specific input, I get this specific output." This test-then-verify loop caught issues that manual testing alone might have missed.
- **What I'd do differently:** Next time I would start by reading the code carefully before asking the AI for help. In this project, I initially asked Copilot to explain bugs before I fully understood the code flow myself, which meant I couldn't always tell if its explanations were accurate. Understanding the code first makes me a better judge of AI suggestions.
- This project showed me that AI-generated code can look perfectly reasonable on the surface while hiding subtle logic bugs (like swapped hint messages or type coercion on alternating attempts). It reinforced that AI is a tool to accelerate my work, not a replacement for carefully reading and testing the code myself.
