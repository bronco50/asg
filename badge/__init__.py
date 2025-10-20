import check50


@check50.check()
def exists():
    """badge.py exists"""
    check50.exists("badge.py")


@check50.check(exists)
def test_name_box():
    """
    input of Benny Bronco yields correctly formatted centered box
    +-----------------+
    |  Bronco, Benny  |
    +-----------------+
    """
    first = "Benny"
    last = "Bronco"

    # Expected strings
    full_name = f"{last}, {first}"
    width = len(full_name) + 4
    expected_top_bottom = "+" + "-" * width + "+"
    expected_middle = "|" + full_name.center(width) + "|"

    # Run student program and capture output
    actual = (
        check50.run("python3 badge.py")
        .stdin(first, prompt=True)
        .stdin(last, prompt=True)
        .stdout()
    )

    # Strip and split output lines
    lines = actual.strip("\n").splitlines()

    # ---------- Check 1: Three total lines ----------
    if len(lines) != 3:
        raise check50.Mismatch(
            "3 lines of output",
            f"{len(lines)} lines found",
            help="Your badge should have exactly three lines: top border, name line, and bottom border.",
        )

    top, middle, bottom = lines

    # ---------- Check 2: Border lengths ----------
    if top != expected_top_bottom or bottom != expected_top_bottom:
        raise check50.Mismatch(
            expected_top_bottom,
            f"{top}\n{bottom}",
            help="Your top and bottom borders must use '+' and '-' and match len(full_name) + 4.",
        )

    # ---------- Check 3: Correct order and comma ----------
    if full_name not in middle:
        raise check50.Mismatch(
            full_name,
            middle,
            help="Be sure to format the name as 'Last, First' (with a comma and a space).",
        )

    # ---------- Check 4: Center alignment ----------
    if middle != expected_middle:
        raise check50.Mismatch(
            expected_middle,
            middle,
            help="Your name must be centered in the box using .center(width).",
        )
