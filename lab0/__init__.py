import check50
import importlib.util
import sys
import os
from math import pi


def load_module(name, path):
    """Generic loader for a module by name and file path."""
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    # Ensure current directory is in sys.path so imports between modules work
    sys.path.append(os.path.dirname(path))
    spec.loader.exec_module(module)
    return module


def load_brickoven():
    """Helper to import brickoven.py safely."""
    return load_module("brickoven", "brickoven.py")


def load_receipt():
    """Helper to import receipt.py safely."""
    return load_module("receipt", "receipt.py")


@check50.check()
def exists():
    """brickoven.py and receipt.py exist"""
    check50.exists("brickoven.py")
    check50.exists("receipt.py")


# ======================
# calculate_pizzas TESTS
# ======================

@check50.check(exists)
def test_calculate_pizzas_standard():
    """calculate_pizzas returns correct tuple for 10 guests"""
    brickoven = load_brickoven()
    receipt = load_receipt()  # <-- ensures receipt.py loads too
    expected = (1, 1, 0)
    actual = brickoven.calculate_pizzas(10)

    if actual != expected:
        help = None
        if sum(actual) < sum(expected):
            help = "Are you allocating enough pizzas to cover all guests?"
        elif sum(actual) > sum(expected):
            help = "You might be over-allocating pizzas."
        raise check50.Mismatch(expected, actual, help=help)

# (All your other tests remain the same)
