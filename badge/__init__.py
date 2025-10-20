import check50


@check50.check()
def exists():
    """badge.py exists"""
    check50.exists("badge.py")


@check50.check(exists)
def test_benny_bronco():
    """
    input of Benny Bronco yields correctly sized badge
    +-------------+
    |Bronco, Benny|
    +-------------+
    """
    first = "Benny"
    last = "Bronco"

    full_name = f"{last}, {first}"
    width = len(full_name)
    expected_top_bottom = "+" + "-" * width + "+"
    expected_middle = "|" + full_name + "|"

    # Run the student's program
    actual = (
        check50.run("python3 badge.py")
        .stdin(first, prompt=True)
        .stdin(last, prompt=True)
        .stdout()
    )

    lines = actual.strip("\n").splitlines()

    # ---------- Check 1: Exactly 3 lines ----------
    if len(lines) != 3:
        raise check50.Mismatch(
            "3 lines of output",
            f"{len(lines)} lines found",
            help="Your output should have exactly three lines: top border, name line, and bottom border.",
        )

    top, middle, bottom = lines

    # ---------- Check 2: Name order ----------
    if full_name not in middle:
        raise check50.Mismatch(
            full_name,
            middle,
            help="Be sure to format the name as 'Last, First' (with a comma and a space).",
        )

    # ---------- Check 3: Top and bottom borders ----------
    if top != expected_top_bottom or bottom != expected_top_bottom:
        raise check50.Mismatch(
            expected_top_bottom,
            f"{top}\n{bottom}",
            help="Your top and bottom borders must use '+' and '-' and match the exact length of the full name.",
        )

    # ---------- Check 4: Proper alignment with borders ----------
    if middle != expected_middle:
        raise check50.Mismatch(
            expected_middle,
            middle,
            help="Make sure there are no extra spaces — your name should align perfectly between the '|' characters.",
        )
