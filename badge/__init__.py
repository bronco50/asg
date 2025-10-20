import check50
import re


@check50.check()
def exists():
    """badge.py exists"""
    check50.exists("badge.py")


@check50.check(exists)
def test_name_box():
    """input of Geno Lewis yields correct centered box"""
    expected = (
        "+---------------+\n"
        "|  Lewis, Geno  |\n"
        "+---------------+\n"
    )

    actual = (
        check50.run("python3 badge.py")
        .stdin("Geno", prompt=True)
        .stdin("Lewis", prompt=True)
        .stdout()
    )

    # If output doesn't match exactly, decide which hint to show
    if not re.search(re.escape(expected), actual):
        help = None

        # Common issues with box spacing and centering
        if "," not in actual:
            help = "Did you forget to include the comma and space in '{last}, {first}'?"
        elif not re.search(r"\|\s+Lewis,\s+Geno\s+\|", actual):
            help = "Are you centering the full name using .center(width)?"
        elif not re.search(r"\+\-+\+", actual):
            help = "Check your top and bottom borders — they should match the width of the name box."
        elif "\n\n" in actual:
            help = "It looks like you have extra blank lines — there should only be three lines."

        raise check50.Mismatch(expected, actual, help=help)
