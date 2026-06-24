from logic_utils import check_guess


def test_winning_guess():
    # Secret 50, guess 50 -> win
    result = check_guess(50, 50)
    assert result[0] == "Win"


def test_guess_too_high():
    # Secret 50, guess 60 -> outcome "Too High"
    result = check_guess(60, 50)
    assert result[0] == "Too High"


def test_guess_too_low():
    # Secret 50, guess 40 -> outcome "Too Low"
    result = check_guess(40, 50)
    assert result[0] == "Too Low"


def test_too_high_hint_says_go_lower():
    # New test: targets the inverted-hint bug I fixed
    result = check_guess(60, 50)
    assert "LOWER" in result[1]