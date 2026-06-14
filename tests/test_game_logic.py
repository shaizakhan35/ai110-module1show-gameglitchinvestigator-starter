from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High" and "Go LOWER"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low" and "Go HIGHER"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_hot_cold_indicator():
    from logic_utils import get_hot_cold_indicator

    assert get_hot_cold_indicator(50, 55) == "🔥"
    assert get_hot_cold_indicator(50, 40) == "🔥"
    assert get_hot_cold_indicator(50, 61) == "🧊"
