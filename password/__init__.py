import check50


@check50.check()
def exists():
    """password.py exists"""
    check50.exists("password.py")


@check50.check(exists)
def test_very_weak_password():
    """'abc123' yields Very Weak"""
    result = (
        check50.run("python3 password.py")
        .stdin("abc123", prompt=True)
        .stdout()
        .strip()
    )
    if "Strength: Very Weak" not in result:
        help = "Passwords shorter than 8 characters should be rated 'Very Weak'."
        raise check50.Mismatch("Strength: Very Weak", result, help=help)


@check50.check(exists)
def test_weak_password():
    """'moonbase123' yields Score: 22 and Strength: Weak"""
    result = (
        check50.run("python3 password.py")
        .stdin("moonbase123", prompt=True)
        .stdout()
        .strip()
    )
    if "Score: 22" not in result:
        help = "Make sure you are assigning the points correctly."
        raise check50.Mismatch("Score: 22", result, help=help)
    if "Strength: Weak" not in result:
        help = "Make sure you are providing the appropriate rating."
        raise check50.Mismatch("Strength: Weak", result, help=help)


@check50.check(exists)
def test_moderate_password():
    """'Mars!2025' yields Score: 30 and Strength: Moderate"""
    result = (
        check50.run("python3 password.py")
        .stdin("Mars!2025", prompt=True)
        .stdout()
        .strip()
    )
    if "Score: 30" not in result:
        help = "Make sure you are assigning the points correctly."
        raise check50.Mismatch("Score: 30", result, help=help)
    if "Strength: Moderate" not in result:
        help = "Make sure you are providing the appropriate rating."
        raise check50.Mismatch("Strength: Moderate", result, help=help)


@check50.check(exists)
def test_strong_password():
    """'LaunchCode2025' yields Score: 38 and Strength: Strong"""
    result = (
        check50.run("python3 password.py")
        .stdin("LaunchCode2025", prompt=True)
        .stdout()
        .strip()
    )
    if "Score: 38" not in result:
        help = "Make sure you are assigning the points correctly."
        raise check50.Mismatch("Score: 38", result, help=help)
    if "Strength: Strong" not in result:
        help = "Make sure you are providing the appropriate rating."
        raise check50.Mismatch("Strength: Strong", result, help=help)


@check50.check(exists)
def test_very_strong_password():
    """'M@r$Expl0r3r2025!' yields Score: 48 and Strength: Very Strong"""
    result = (
        check50.run("python3 password.py")
        .stdin("M@r$Expl0r3r2025!", prompt=True)
        .stdout()
        .strip()
    )
    if "Score: 48" not in result:
        help = "Make sure you are assigning the points correctly."
        raise check50.Mismatch("Score: 48", result, help=help)
    if "Strength: Very Strong" not in result:
        help = "Make sure you are providing the appropriate rating."
        raise check50.Mismatch("Strength: Very Strong", result, help=help)
