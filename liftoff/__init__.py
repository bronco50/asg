import check50
from re import escape

# Adds case insensitivity for output matching
case_insensitive_prefix = "(?i)"


@check50.check()
def exists():
    """liftoff.py exists"""
    check50.exists("liftoff.py")


@check50.check(exists)
def test_countdown_down():
    """input direction 'd' and number 3 prints 3, 2, 1, and Liftoff!"""
    expected = "Direction (a/d): Countdown: 3\n2\n1\nLiftoff!"
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
def test_countdown_up():
    """input direction 'a' and number 3 prints 1, 2, 3, and Liftoff!"""
    expected = "Direction (a/d): Countdown: 1\n2\n3\nLiftoff!"
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
def test_countdown_down_large():
    """input direction 'd' and number 5 prints 5 down to 1 and Liftoff!"""
    expected = "Direction (a/d): Countdown: 5\n4\n3\n2\n1\nLiftoff!"
    result = (
        check50.run("python3 liftoff.py")
        .stdin("d", prompt=True)
        .stdin("5", prompt=True)
        .stdout()
        .strip()
    )
    if result != expected.strip():
        help = (
            "Be sure your countdown loop works for larger values of n. "
            "For direction 'd' and n = 5, output should be:\n5\n4\n3\n2\n1\nLiftoff!"
        )
        raise check50.Mismatch(expected.strip(), result, help=help)


@check50.check(exists)
def test_countdown_up_large():
    """input direction 'a' and number 5 prints 1 up to 5 and Liftoff!"""
    expected = "Direction (a/d): Countdown: 1\n2\n3\n4\n5\nLiftoff!"
    result = (
        check50.run("python3 liftoff.py")
        .stdin("a", prompt=True)
        .stdin("5", prompt=True)
        .stdout()
        .strip()
    )
    if result != expected.strip():
        help = (
            "Be sure your count-up loop works correctly. "
            "For direction 'a' and n = 5, output should be:\n1\n2\n3\n4\n5\nLiftoff!"
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
def test_negative_number():
    """input direction 'a' and number -3 yields Invalid"""
    result = (
        check50.run("python3 liftoff.py")
        .stdin("a", prompt=True)
        .stdin("-3", prompt=True)
        .stdout()
        .strip()
    )
    if "invalid" not in result.lower():
        help = (
            "If the number entered is less than 0, your program should print 'Invalid' "
            "and stop — it should not attempt to count up or down."
        )
        raise check50.Mismatch("Invalid", result, help=help)


@check50.check(exists)
def test_zero():
    """input of 0 prints only Liftoff! for both directions"""
    for direction in ["a", "d"]:
        result = (
            check50.run("python3 liftoff.py")
            .stdin(direction, prompt=True)
            .stdin("0", prompt=True)
            .stdout()
            .strip()
        )
        if result.lower() != "direction (a/d): countdown: liftoff!".lower() and result.lower() != "liftoff!".lower():
            help = (
                "If the user enters 0, print only 'Liftoff!' — no numbers before it. "
                "This applies to both directions ('a' and 'd')."
            )
            raise check50.Mismatch("Liftoff!", result, help=help)
