import check50
import importlib.util
from math import pi


def load_brickoven():
    """Helper to import brickoven.py safely."""
    spec = importlib.util.spec_from_file_location("brickoven", "brickoven.py")
    brickoven = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(brickoven)
    return brickoven


@check50.check()
def exists():
    """brickoven.py exists"""
    check50.exists("brickoven.py")


# ======================
# calculate_pizzas TESTS
# ======================

@check50.check(exists)
def test_calculate_pizzas_standard():
    """calculate_pizzas returns correct tuple for 10 guests"""
    brickoven = load_brickoven()
    expected = (1, 1, 0)
    actual = brickoven.calculate_pizzas(10)

    if actual != expected:
        help = None
        if sum(actual) < sum(expected):
            help = "Are you allocating enough pizzas to cover all guests?"
        elif sum(actual) > sum(expected):
            help = "You might be over-allocating pizzas."
        raise check50.Mismatch(expected, actual, help=help)


@check50.check(exists)
def test_calculate_pizzas_edge():
    """calculate_pizzas handles small and large groups correctly"""
    brickoven = load_brickoven()
    expected_small = (0, 0, 1)
    actual_small = brickoven.calculate_pizzas(1)
    if actual_small != expected_small:
        raise check50.Mismatch(expected_small, actual_small, help="For 1 guest, return 1 small pizza only.")

    expected_large = (2, 0, 1)  # 15 guests → 2 large (14), 1 small (1 left)
    actual_large = brickoven.calculate_pizzas(15)
    if actual_large != expected_large:
        raise check50.Mismatch(expected_large, actual_large, help="Be sure to handle 15+ guests (two large pizzas feed 14).")


# ======================
# serving_size TESTS
# ======================

@check50.check(exists)
def test_serving_size_normal():
    """serving_size returns correct total area for 1 of each size"""
    brickoven = load_brickoven()
    expected = pi * (10**2) + pi * (8**2) + pi * (6**2)
    actual = brickoven.serving_size(1, 1, 1)
    if abs(actual - expected) > 0.01:
        help = None
        if actual == 0:
            help = "Did you remember to calculate area = π × r² for each pizza?"
        elif actual < expected:
            help = "It looks like one or more pizza sizes were missed in your total."
        raise check50.Mismatch(round(expected, 2), round(actual, 2), help=help)


@check50.check(exists)
def test_serving_size_zero():
    """serving_size returns 0 when no pizzas are ordered"""
    brickoven = load_brickoven()
    expected = 0
    actual = brickoven.serving_size(0, 0, 0)
    if actual != expected:
        raise check50.Mismatch(expected, actual, help="If all counts are 0, return 0 area.")


# ======================
# apply_discount TESTS
# ======================

@check50.check(exists)
def test_apply_discount_standard():
    """apply_discount applies correct rate for 12 guests"""
    brickoven = load_brickoven()
    subtotal = 100.0
    expected = (90.0, 0.10)
    actual = brickoven.apply_discount(subtotal, 12)
    if actual != expected:
        help = None
        if actual[1] == 0:
            help = "Are you applying a 10% discount for 10–14 guests?"
        raise check50.Mismatch(expected, actual, help=help)


@check50.check(exists)
def test_apply_discount_edge():
    """apply_discount applies correct rate for 16 guests and small group"""
    brickoven = load_brickoven()
    subtotal = 200.0

    expected_large = (170.0, 0.15)
    actual_large = brickoven.apply_discount(subtotal, 16)
    if actual_large != expected_large:
        raise check50.Mismatch(expected_large, actual_large, help="15+ guests should get 15% off.")

    expected_small = (subtotal, 0.0)
    actual_small = brickoven.apply_discount(subtotal, 3)
    if actual_small != expected_small:
        raise check50.Mismatch(expected_small, actual_small, help="Groups under 5 should not get any discount.")


# ======================
# calculate_cost TESTS
# ======================

@check50.check(exists)
def test_calculate_cost_normal():
    """calculate_cost returns correct tax, tip, and total for 10% tip"""
    brickoven = load_brickoven()
    subtotal = 100.0
    expected_tax = subtotal * 0.1025
    expected_tip = subtotal * 0.10
    expected_total = subtotal + expected_tax + expected_tip
    expected = (round(expected_tax, 2), round(expected_tip, 2), round(expected_total, 2))
    actual = brickoven.calculate_cost(subtotal, 10.0)

    if not isinstance(actual, tuple) or len(actual) != 3 or any(abs(a - e) > 0.02 for a, e in zip(actual, expected)):
        help = "Tax = subtotal × 10.25%, Tip = subtotal × (tip% ÷ 100), Total = subtotal + tax + tip."
        raise check50.Mismatch(expected, tuple(round(v, 2) for v in actual), help=help)


@check50.check(exists)
def test_calculate_cost_edge():
    """calculate_cost handles zero tip correctly"""
    brickoven = load_brickoven()
    subtotal = 50.0
    expected_tax = subtotal * 0.1025
    expected_tip = 0
    expected_total = subtotal + expected_tax
    expected = (round(expected_tax, 2), expected_tip, round(expected_total, 2))
    actual = brickoven.calculate_cost(subtotal, 0.0)

    if any(abs(a - e) > 0.02 for a, e in zip(actual, expected)):
        help = "Even with 0% tip, still include the 10.25% sales tax."
        raise check50.Mismatch(expected, tuple(round(v, 2) for v in actual), help=help)
