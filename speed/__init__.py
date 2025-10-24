import check50

@check50.check()
def exists():
    """speed.py exists"""
    check50.exists("speed.py")


@check50.check(exists)
def test_school_zone():
    """correct fines for SCHOOL zone"""
    tests = [
        (20, "$0"),     # at limit
        (25, "$100"),   # 5 mph over
        (35, "$250"),   # 15 mph over
        (50, "$500")    # 30 mph over
    ]
    for speed, expected in tests:
        result = check50.run("python3 speed.py").stdin(str(speed)).stdin("SCHOOL").stdout().strip()
        if result != expected:
            help = None
            if result.replace("$", "").isdigit() and result != expected:
                help = f"Check SCHOOL fine for {speed} mph."
            elif "$" not in result:
                help = "Remember to include the '$' in your output."
            raise check50.Mismatch(expected, result, help=help)


@check50.check(exists)
def test_city_zone():
    """correct fines for CITY zone"""
    tests = [
        (30, "$0"),     # at limit
        (35, "$75"),    # 5 mph over
        (45, "$200"),   # 15 mph over
        (60, "$400")    # 30 mph over
    ]
    for speed, expected in tests:
        result = check50.run("python3 speed.py").stdin(str(speed)).stdin("CITY").stdout().strip()
        if result != expected:
            help = None
            if "$" not in result:
                help = "Output must include the '$' symbol."
            else:
                help = f"Verify CITY fines at {speed} mph follow the fine schedule."
            raise check50.Mismatch(expected, result, help=help)


@check50.check(exists)
def test_highway_zone():
    """correct fines for HIGHWAY zone"""
    tests = [
        (65, "$0"),     # at limit
        (70, "$50"),    # 5 mph over
        (80, "$150"),   # 15 mph over
        (90, "$300")    # 25 mph over
    ]
    for speed, expected in tests:
        result = check50.run("python3 speed.py").stdin(str(speed)).stdin("HIGHWAY").stdout().strip()
        if result != expected:
            help = None
            if "$" not in result:
                help = "Your output should include the '$' sign before the number."
            else:
                help = f"Check HIGHWAY fine logic for {speed} mph."
            raise check50.Mismatch(expected, result, help=help)


@check50.check(exists)
def test_case_sensitivity():
    """handles lowercase input gracefully"""
    result = check50.run("python3 speed.py").stdin("40").stdin("city").stdout().strip()
    if result not in ["$75", "$0", "$200", "$400"]:
        raise check50.Failure("Make sure your program accounts for lowercase zone names (e.g., use .upper()).")


@check50.check(exists)
def test_edge_cases():
    """handles boundary values correctly"""
    edge_tests = [
        ("SCHOOL", 30, "$100"),  # exactly 10 mph over
        ("CITY", 40, "$75"),     # exactly 10 mph over
        ("HIGHWAY", 75, "$50")   # exactly 10 mph over
    ]
    for zone, speed, expected in edge_tests:
        result = check50.run("python3 speed.py").stdin(str(speed)).stdin(zone).stdout().strip()
        if result != expected:
            help = f"Double-check your 'less than or equal to' logic for {zone} zone at {speed} mph."
            raise check50.Mismatch(expected, result, help=help)
