from logic_utils import check_guess, parse_guess


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

def test_parse_rejects_negative_text_gracefully():
    # Negative numbers parse as valid ints (no crash)
    ok, value, err = parse_guess("-5")
    assert ok is True and value == -5


def test_parse_handles_decimal_input():
    # Decimals get truncated to int, not crashed
    ok, value, err = parse_guess("42.9")
    assert ok is True and value == 42


def test_parse_handles_very_large_number():
    # Large values don't overflow or crash
    ok, value, err = parse_guess("999999999999")
    assert ok is True and value == 999999999999


def test_parse_rejects_empty_string():
    ok, value, err = parse_guess("")
    assert ok is False and value is None