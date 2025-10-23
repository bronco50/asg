import check50


@check50.check()
def exists():
    """parity.py exists"""
    check50.exists("parity.py")


@check50.check(exists)
def test_odd():
    """prints ODD when number is odd"""
    result = check50.run("python3 parity.py").stdin("13").stdout().strip()
    expected = "ODD"
    if result != expected:
        help = None
        if result.lower() == "odd":
            help = "Make sure the output is in all caps."
        else:
            help = "Use % to check if a number is even or odd."
        raise check50.Mismatch(expected, result, help=help)


@check50.check(exists)
def test_even():
    """prints EVEN when number is even"""
    result = check50.run("python3 parity.py").stdin("8").stdout().strip()
    expected = "EVEN"
    if result != expected:
        help = None
        if result.lower() == "even":
            help = "Make sure the output is in all caps."
        else:
            help = "Use % to check if a number is even or odd."
        raise check50.Mismatch(expected, result, help=help)
