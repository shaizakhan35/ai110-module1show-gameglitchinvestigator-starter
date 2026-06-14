def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        # Allow floats like "4.0" to be entered
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def get_hot_cold_indicator(guess, secret):
    """
    Return a hot/cold emoji based on how close the guess is to the secret.

    🔥 when within 10, 🧊 when far away.
    """
    try:
        secret_int = int(secret)
        guess_int = int(guess)
    except Exception:
        return "🧊"

    return "🔥" if abs(guess_int - secret_int) <= 10 else "🧊"


# FIX: Refactored check_guess from app.py into logic_utils.py, fixed swapped hint messages using agent mode
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Normalize secret to an int when possible so comparisons behave correctly.
    try:
        secret_int = int(secret)
    except Exception:
        secret_int = None

    # FIXME: Logic breaks here
    # FIX: AI identified swapped hint messages, corrected using chat mode Too High now says Go LOWER and Too Low says Go HIGHER
    if secret_int is not None:
        if guess == secret_int:
            return "Win", "🎉 Correct!"
        if guess > secret_int:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"

    # Fallback to string comparison if secret is not numeric
    try:
        g = str(guess)
        if g == secret:
            return "Win", "🎉 Correct!"
        if g > secret:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"
    except Exception:
        return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
