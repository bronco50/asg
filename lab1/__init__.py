import check50
import check50.internal
import importlib.util
import sys
import os
from contextlib import contextmanager
from io import StringIO


# ============================================================
# Helper: Load Module
# ============================================================

def load_wordle():
    """Imports wordle.py safely."""
    spec = importlib.util.spec_from_file_location("wordle", "wordle.py")
    module = importlib.util.module_from_spec(spec)
    sys.path.append(os.getcwd())
    spec.loader.exec_module(module)
    return module


# ============================================================
# Helper: mock input
# ============================================================

@contextmanager
def mock_inputs(inputs):
    """
    Simulates user sequential input for functions relying on input().
    """
    input_iter = iter(inputs)

    def fake_input(prompt=""):
        return next(input_iter)

    old_input = __builtins__["input"]
    __builtins__["input"] = fake_input
    try:
        yield
    finally:
        __builtins__["input"] = old_input


# ============================================================
# Helper: Capture stdout
# ============================================================

@contextmanager
def capture_output():
    old_out = sys.stdout
    sys.stdout = StringIO()
    try:
        yield sys.stdout
    finally:
        sys.stdout = old_out


# ============================================================
# EXISTS TEST
# ============================================================

@check50.check()
def exists():
    """wordle.py exists"""
    check50.exists("wordle.py")
    check50.exists("wordlist.txt")


# ============================================================
# Task 1: has_won(secret, guess)
# ============================================================

@check50.check(exists)
def test_has_won_basic():
    """has_won returns correct True/False for matching words"""
    wordle = load_wordle()

    if not wordle.has_won("crane", "crane"):
        raise check50.Mismatch("True", "False", help="Matching words should return True.")

    if wordle.has_won("crane", "plane"):
        raise check50.Mismatch("False", "True", help="Non-matching words should return False.")


@check50.check(exists)
def test_has_won_case_insensitive():
    """has_won treats case-insensitive matches as win"""
    wordle = load_wordle()

    if not wordle.has_won("crane", "CRANE"):
        raise check50.Mismatch("True", "False", help="Guess should be treated case-insensitively.")


# ============================================================
# Task 2: get_player_guess(word_list)
# ============================================================

@check50.check(exists)
def test_get_player_guess_multiple_invalid():
    """get_player_guess rejects invalid guesses until valid"""

    wordle = load_wordle()
    word_list = {"crane", "plane", "abcde"}

    with mock_inputs(["cr4ne", "cranee", "hello", "crane"]):
        with capture_output() as out:
            guess = wordle.get_player_guess(word_list)

    if guess.lower() != "crane":
        raise check50.Mismatch("crane", guess, help="Ensure input validation loop continues until a valid guess.")


# ============================================================
# Task 3: give_feedback(secret, guess)
# ============================================================

@check50.check(exists)
def test_feedback_exact_match():
    """give_feedback returns all greens for exact match"""

    wordle = load_wordle()
    feedback = wordle.give_feedback("crane", "crane")

    if feedback != "🟩🟩🟩🟩🟩":
        raise check50.Mismatch("🟩🟩🟩🟩🟩", feedback)


@check50.check(exists)
def test_feedback_mixed():
    """give_feedback returns correct mix of green/yellow/white"""

    wordle = load_wordle()
    feedback = wordle.give_feedback("crane", "cakes")

    expected = "🟩⬜⬜🟨⬜"
    if feedback != expected:
        raise check50.Mismatch(expected, feedback, help="Check letter position and presence logic.")


# ============================================================
# Task 4: display_game_state(guess, feedback)
# ============================================================

@check50.check(exists)
def test_display_game_state():
    """display_game_state prints correct formatted output"""

    wordle = load_wordle()
    guess = "crane"
    fb = "🟩🟩🟩⬜🟩"

    with capture_output() as out:
        wordle.display_game_state(guess, fb)

    printed = out.getvalue().strip()
    expected = "CRANE | 🟩🟩🟩⬜🟩"

    if printed != expected:
        raise check50.Mismatch(expected, printed, help="Ensure uppercase guess and correct formatting.")


# ============================================================
# Full Game Simulation — Task 5
# ============================================================

def normalize_output(text):
    """Normalizes whitespace for easier matching."""
    return "\n".join(line.rstrip() for line in text.strip().split("\n"))


# -----------------------------
# RUN A — Secret = mango
# -----------------------------

@check50.check(exists)
def test_play_wordle_run_a():
    """play_wordle correctly handles Sample Run A (secret=mango)"""

    wordle = load_wordle()
    word_list = {"green", "tower", "clamp", "mania", "mango"}

    inputs = ["green", "tower", "clamp", "mania", "mango"]

    with mock_inputs(inputs):
        with capture_output() as out:
            wordle.play_wordle("mango", word_list)

    output = normalize_output(out.getvalue())

    required_lines = [
        "GREEN | ⬜⬜⬜⬜⬜",
        "5 guesses left.",
        "TOWER | ⬜⬜⬜⬜⬜",
        "4 guesses left.",
        "CLAMP | ⬜⬜⬜🟨⬜",
        "3 guesses left.",
        "MANIA | 🟩🟨🟨⬜🟨",
        "2 guesses left.",
        "MANGO | 🟩🟩🟩🟩🟩",
        "Congrats! You've solved today's challenge!"
    ]

    for line in required_lines:
        if line not in output:
            raise check50.Mismatch("Expected output line", line, help=f"Missing line: {line}")


# -----------------------------
# RUN B — Secret = mango
# -----------------------------

@check50.check(exists)
def test_play_wordle_run_b():
    """play_wordle correctly handles Sample Run B (secret=mango)"""

    wordle = load_wordle()
    word_list = {"sheep", "round", "clamp", "among", "manor", "magic", "mango"}

    inputs = ["sheep", "round", "clamp", "among", "manor", "magic"]

    with mock_inputs(inputs):
        with capture_output() as out:
            wordle.play_wordle("mango", word_list)

    output = normalize_output(out.getvalue())

    required_lines = [
        "SHEEP | ⬜⬜⬜⬜⬜",
        "5 guesses left.",
        "ROUND | ⬜🟨⬜🟨⬜",
        "4 guesses left.",
        "CLAMP | ⬜⬜🟨🟨⬜",
        "3 guesses left.",
        "AMONG | 🟨🟨🟨🟨🟨",
        "2 guesses left.",
        "MANOR | 🟩🟩🟩🟨⬜",
        "1 guess left.",
        "MAGIC | 🟩🟩🟨⬜⬜",
        "0 guesses left.",
        "Game Over! The word was: mango"
    ]

    for line in required_lines:
        if line not in output:
            raise check50.Mismatch("Expected output line", line, help=f"Missing line: {line}")
