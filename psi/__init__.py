import check50


@check50.check()
def exists():
    """psi.py exists"""
    check50.exists("psi.py")


@check50.check(exists)
def test_invalid():
    """prints INVALID PRESSURE for negative PSI"""
    result = check50.run("python3 psi.py").stdin("-5").stdout().strip()
    expected = "INVALID PRESSURE"
    if result != expected:
        help = "Be sure to check for negative PSI values first."
        raise check50.Mismatch(expected, result, help=help)


@check50.check(exists)
def test_dangerously_high():
    """prints PRESSURE DANGEROUSLY HIGH for PSI ≥ 40"""
    result = check50.run("python3 psi.py").stdin("42").stdout().strip()
    expected = "PRESSURE DANGEROUSLY HIGH"
    if result != expected:
        help = "Check your condition order; PSI 40+ should print DANGEROUSLY HIGH."
        raise check50.Mismatch(expected, result, help=help)


@check50.check(exists)
def test_high():
    """prints PRESSURE HIGH for PSI between 35–39.9"""
    result = check50.run("python3 psi.py").stdin("36").stdout().strip()
    expected = "PRESSURE HIGH"
    if result != expected:
        help = "Be sure PSI values between 35 and 39.9 print HIGH."
        raise check50.Mismatch(expected, result, help=help)


@check50.check(exists)
def test_normal():
    """prints PRESSURE NORMAL for PSI between 30–34.9"""
    result = check50.run("python3 psi.py").stdin("32").stdout().strip()
    expected = "PRESSURE NORMAL"
    if result != expected:
        help = "Check that PSI between 30 and 34.9 prints NORMAL."
        raise check50.Mismatch(expected, result, help=help)


@check50.check(exists)
def test_low():
    """prints PRESSURE LOW for PSI between 28–29.9"""
    result = check50.run("python3 psi.py").stdin("28.5").stdout().strip()
    expected = "PRESSURE LOW"
    if result != expected:
        help = "Be sure PSI between 28 and 29.9 prints LOW."
        raise check50.Mismatch(expected, result, help=help)


@check50.check(exists)
def test_dangerously_low():
    """prints PRESSURE DANGEROUSLY LOW for PSI < 28"""
    result = check50.run("python3 psi.py").stdin("25").stdout().strip()
    expected = "PRESSURE DANGEROUSLY LOW"
    if result != expected:
        help = "Be sure PSI below 28 prints DANGEROUSLY LOW."
        raise check50.Mismatch(expected, result, help=help)
