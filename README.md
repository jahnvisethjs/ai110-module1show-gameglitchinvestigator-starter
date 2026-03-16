# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game purpose:** A Streamlit-based number guessing game where you pick a difficulty, guess a secret number within a limited number of attempts, and receive hints ("Too High" / "Too Low") to guide you. Your score is tracked across guesses.
- [x] **Bugs found:**
  1. Hint messages were reversed — guessing too high said "Go HIGHER!" instead of "Go LOWER!"
  2. Hard mode range (1–50) was actually easier than Normal mode (1–100)
  3. On even-numbered attempts, the secret was converted to a string, breaking comparisons
  4. Score changed erratically — "Too High" gave +5 on even attempts but -5 on odd
  5. Attempts counter started at 1 instead of 0, costing one attempt from the start
- [x] **Fixes applied:**
  1. Swapped the hint messages in `check_guess()` so "Too High" says "Go LOWER!" and vice versa
  2. Changed Hard mode range to 1–200
  3. Removed the string conversion — secret is always compared as an integer
  4. Made wrong-guess penalties a consistent -5 regardless of attempt number
  5. Changed initial attempts to 0 and fixed the "Attempts left" display
  6. Refactored all game logic from `app.py` into `logic_utils.py`
  7. Fixed the info bar to show the actual difficulty range instead of hardcoded "1 and 100"

## 📸 Demo

- [ ] [Insert a screenshot of your fixed, winning game here]

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
