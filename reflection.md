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

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
