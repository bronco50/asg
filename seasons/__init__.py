import check50

@check50.check()
def exists():
    """seasons.py exists"""
    check50.exists("seasons.py")


@check50.check(exists)
def test_seasons():
    """prints correct season for each representative month"""
    tests = {
        "January": "WINTER",
        "April": "SPRING",
        "July": "SUMMER",
        "October": "AUTUMN"
    }

    for month, expected in tests.items():
        result = check50.run("python3 seasons.py").stdin(month).stdout().strip()
        if result != expected:
            help = None
            if result.lower() == expected.lower():
                help = "Make sure the output is in ALL CAPS."
            else:
                help = f"Check that {month} correctly maps to {expected}."
            raise check50.Mismatch(expected, result, help=help)
