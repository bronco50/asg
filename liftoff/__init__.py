import check50


@check50.check()
def exists():
    """liftoff.py exists"""
    check50.exists("liftoff.py")


@check50.check(exists)
def test_countdown_down_three():
    """input direction 'd' and number 3 prints 3, 2, 1, and Liftoff!"""
    expected = "3\n2\n1\nLiftoff!"
    result = (
        check50.run("python3 liftoff.py")
        .stdin("d", prompt=True)
        .stdin("3", prompt=True)
        .stdout()
        .strip()
    )
    if result != expected.strip():
        help = (
            "When direction is 'd', your program should count down from n to 1, "
            "printing each number on its own line, followed by 'Liftoff!'.\n\n"
            "Example output for n = 3:\n3\n2\n1\nLiftoff!"
        )
        raise check50.Mismatch(expected.strip(), result, help=help)


@check50.check(exists)
def test_countdown_down_four():
    """input direction 'd' and number 4 prints 4, 3, 2, 1, and Liftoff!"""
    expected = "4\n3\n2\n1\nLiftoff!"
    result = (
        check50.run("python3 liftoff.py")
        .stdin("d", prompt=True)
        .stdin("4", prompt=True)
        .stdout()
        .strip()
    )
    if result != expected.strip():
        help = (
            "Ensure your countdown loop handles other values correctly. "
            "For direction 'd' and n = 4, expected:\n4\n3\n2\n1\nLiftoff!"
        )
        raise check50.Mismatch(expected.strip(), result, help=help)


@check50.check(exists)
def test_countdown_up_three():
    """input direction 'a' and number 3 prints 1, 2, 3, and Liftoff!"""
    expected = "1\n2\n3\nLiftoff!"
    result = (
        check50.run("python3 liftoff.py")
        .stdin("a", prompt=True)
        .stdin("3", prompt=True)
        .stdout()
        .strip()
    )
    if result != expected.strip():
        help = (
            "When direction is 'a', your program should count up from 1 to n, "
            "printing each number on its own line, followed by 'Liftoff!'.\n\n"
            "Example output for n = 3:\n1\n2\n3\nLiftoff!"
        )
        raise check50.Mismatch(expected.strip(), result, help=help)


@check50.check(exists)
def test_countdown_up_seven():
    """input direction 'a' and number 7 prints 1 through 7 and Liftoff!"""
    expected = "1\n2\n3\n4\n5\n6\n7\nLiftoff!"
    result = (
        check50.run("python3 liftoff.py")
        .stdin("a", prompt=True)
        .stdin("7", prompt=True)
        .stdout()
        .strip()
    )
    if result != expected.strip():
        help = (
            "Check that your loop correctly prints all numbers up to n. "
            "For direction 'a' and n = 7, expected:\n1\n2\n3\n4\n5\n6\n7\nLiftoff!"
        )
        raise check50.Mismatch(expected.strip(), result, help=help)


@check50.check(exists)
def test_invalid_direction():
    """input direction 'x' yields Invalid"""
    result = (
        check50.run("python3 liftoff.py")
        .stdin("x", prompt=True)
        .stdin("3", prompt=True)
        .stdout()
        .strip()
    )
    if "invalid" not in result.lower():
        help = (
            "If the direction is not 'a' or 'd', your program should print 'Invalid' "
            "and stop — no countdown should occur."
        )
        raise check50.Mismatch("Invalid", result, help=help)


@check50.check(exists)
def test_nonpositive_number():
    """input number <= 0 yields Invalid"""
    for direction in ["a", "d"]:
        for number in ["0", "-3"]:
            result = (
                check50.run("python3 liftoff.py")
                .stdin(direction, prompt=True)
                .stdin(number, prompt=True)
                .stdout()
                .strip()
            )
            if "invalid" not in result.lower():
                help = (
                    "If the number entered is less than or equal to 0, "
                    "your program should print 'Invalid' and stop — "
                    "no countdown should occur."
                )
                raise check50.Mismatch("Invalid", result, help=help)
