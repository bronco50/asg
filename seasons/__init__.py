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
                if expected == "WINTER":
                    help = "December, January, and February should print WINTER."
                elif expected == "SPRING":
                    help = "March, April, and May should print SPRING."
                elif expected == "SUMMER":
                    help = "June, July, and August should print SUMMER."
                elif expected == "AUTUMN":
                    help = "September, October, and November should print AUTUMN."
            raise check50.Mismatch(expected, result, help=help)
