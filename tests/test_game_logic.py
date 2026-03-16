from logic_utils import check_guess, update_score, get_range_for_difficulty, parse_guess

# --- Existing starter tests (fixed to match tuple return) ---

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# --- New tests for bug fixes ---

def test_hint_message_when_too_high():
    """Verify the hint says 'LOWER' when the guess is too high."""
    outcome, message = check_guess(60, 50)
    assert "LOWER" in message

def test_hint_message_when_too_low():
    """Verify the hint says 'HIGHER' when the guess is too low."""
    outcome, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_hard_range_is_larger_than_normal():
    """Hard mode should have a wider range than Normal."""
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high

def test_score_deduction_is_consistent():
    """Wrong guesses should always deduct points, regardless of attempt number."""
    score_even = update_score(100, "Too High", 2)
    score_odd = update_score(100, "Too High", 3)
    assert score_even == score_odd == 95

def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None

def test_parse_guess_non_numeric():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a number."
