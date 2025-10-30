import check50


@check50.check()
def exists():
    """password.py exists"""
    check50.exists("password.py")


@check50.check(exists)
def test_weak_password():
    """'moonbase123' yields Score: 22 and Strength: Weak"""
    result = (
        check50.run("python3 password.py")
        .stdin("moonbase123", prompt=True)
        .stdout()
        .strip()
    )
    if "Score: 22" not in result or "Strength: Weak" not in result:
        help = (
            "Be sure to add half the length of the password (len(password)//2) "
            "and points per character: +2 uppercase, +1 lowercase, +3 digit, +4 special."
        )
        raise check50.Mismatch("Score: 22\nStrength: Weak", result, help=help)


@check50.check(exists)
def test_moderate_password():
    """'Mars!2025' yields Score: 35 and Strength: Moderate"""
    result = (
        check50.run("python3 password.py")
        .stdin("Mars!2025", prompt=True)
        .stdout()
        .strip()
    )
    if "Score: 35" not in result or "Strength: Moderate" not in result:
        help = (
            "Be sure to add half the length of the password (len(password)//2) "
            "and points per character: +2 uppercase, +1 lowercase, +3 digit, +4 special."
        )
        raise check50.Mismatch("Score: 35\nStrength: Moderate", result, help=help)


@check50.check(exists)
def test_strong_password():
    """'LaunchCode2025' yields Strong classification"""
    result = (
        check50.run("python3 password.py")
        .stdin("LaunchCode2025", prompt=True)
        .stdout()
        .strip()
    )
    if "Strength: Strong" not in result:
        help = (
            "Be sure to add half the length of the password (len(password)//2) "
            "and points per character: +2 uppercase, +1 lowercase, +3 digit, +4 special."
        )
        raise check50.Mismatch("Strength: Strong", result, help=help)


@check50.check(exists)
def test_very_strong_password():
    """'M@r$Expl0r3r2025!' yields Score: 60 and Strength: Very Strong"""
    result = (
        check50.run("python3 password.py")
        .stdin("M@r$Expl0r3r2025!", prompt=True)
        .stdout()
        .strip()
    )
    if "Score: 60" not in result or "Strength: Very Strong" not in result:
        help = (
            "Be sure to add half the length of the password (len(password)//2) "
            "and points per character: +2 uppercase, +1 lowercase, +3 digit, +4 special."
        )
        raise check50.Mismatch("Score: 60\nStrength: Very Strong", result, help=help)
