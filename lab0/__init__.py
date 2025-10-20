import check50
import importlib.util
from math import pi


@check50.check()
def exists():
    """reciept.py exists"""
    check50.exists("reciept.py")


@check50.check(exists)
def test_calculate_pizzas():
    """calculate_pizzas returns correct tuple for 10 guests"""
    spec = importlib.util.spec_from_file_location("reciept", "reciept.py")
    reciept = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reciept)

    expected = (1, 1, 0)  # 1 large feeds 7, 1 medium feeds 3
    actual = reciept.calculate_pizzas(10)

    if actual != expected:
        help = None
        if isinstance(actual, tuple) and sum(actual) < sum(expected):
            help = "Are you allocating enough pizzas to cover all guests?"
        elif isinstance(actual, tuple) and sum(actual) > sum(expected):
            help = "You might be over-allocating pizzas."
        raise check50.Mismatch(expected, actual, help=help)


@check50.check(exists)
def test_serving_size():
    """serving_size returns correct total area for 1 large, 1 medium, 1 small"""
    spec = importlib.util.spec_from_file_location("reciept", "reciept.py")
    reciept = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reciept)

    expected = pi * (10**2) + pi * (8**2) + pi * (6**2)
    actual = reciept.serving_size(1, 1, 1)

    if not isinstance(actual, (int, float)) or abs(actual - expected) > 0.01:
        help = None
        if actual == 0:
            help = "Did you remember to calculate each pizza’s area using π × r²?"
        elif actual < expected:
            help = "It looks like one or more pizza sizes were missed in your total."
        elif actual > expected:
            help = "Double-check that you’re not squaring or summing incorrectly."
        raise check50.Mismatch(round(expected, 2), round(actual, 2), help=help)


@check50.check(exists)
def test_apply_discount():
    """apply_discount applies correct rate for 12 guests"""
    spec = importlib.util.spec_from_file_location("reciept", "reciept.py")
    reciept = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reciept)

    subtotal = 100.0
    expected = (90.0, 0.10)  # 10% off for 10–14 guests
    actual = reciept.apply_discount(subtotal, 12)

    if actual != expected:
        help = None
        if actual[1] == 0:
            help = "Are you applying a 10% discount for groups of 10–14 guests?"
        elif actual[1] < 0.10:
            help = "Double-check your percentage — it should reduce subtotal by 10%."
        elif actual[1] > 0.10:
            help = "Looks like you gave too much discount — confirm your group size ranges."
        raise check50.Mismatch(expected, actual, help=help)


@check50.check(exists)
def test_calculate_cost():
    """calculate_cost returns correct tax, tip, and total for 10% tip"""
    spec = importlib.util.spec_from_file_location("reciept", "reciept.py")
    reciept = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(reciept)

    discounted_subtotal = 100.0
    tip_percentage = 10.0
    expected_tax = discounted_subtotal * 0.1025
    expected_tip = discounted_subtotal * 0.10
    expected_total = discounted_subtotal + expected_tax + expected_tip
    expected = (round(expected_tax, 2), round(expected_tip, 2), round(expected_total, 2))

    actual = reciept.calculate_cost(discounted_subtotal, tip_percentage)

    # Handle incorrect results
    if not isinstance(actual, tuple) or len(actual) != 3:
        raise check50.Mismatch(expected, actual, help="Return (tax, tip, total) as a tuple of three numbers.")
    if any(abs(a - e) > 0.02 for a, e in zip(actual, expected)):
        help = None
        if actual[0] == 0:
            help = "Did you calculate the tax as subtotal × 0.1025?"
        elif actual[1] == 0:
            help = "Did you calculate the tip as subtotal × (tip_percentage ÷ 100)?"
        elif abs(actual[2] - expected_total) < 0.02:
            help = "Be sure total = subtotal + tax + tip."
        raise check50.Mismatch(expected, tuple(round(x, 2) for x in actual), help=help)
