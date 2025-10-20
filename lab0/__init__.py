import check50
import importlib


@check50.check()
def exists():
    """reciept.py exists"""
    check50.exists("reciept.py")


@check50.check(exists)
def test_calculate_pizzas():
    """calculate_pizzas returns correct tuple for 10 guests"""
    reciept = importlib.import_module("reciept")

    expected = (1, 1, 0)  # 1 large (feeds 7), 1 medium (feeds 3)
    actual = reciept.calculate_pizzas(10)

    if actual != expected:
        help = None
        if isinstance(actual, tuple) and sum(actual) < sum(expected):
            help = "Are you allocating enough pizzas to cover all guests?"
        elif isinstance(actual, tuple) and sum(actual) > sum(expected):
            help = "You might be over-allocating pizzas."
        raise check50.Mismatch(expected, actual, help=help)
