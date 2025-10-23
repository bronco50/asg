import check50

@check50.check()
def exists():
    """rental.py exists"""
    check50.exists("rental.py")


@check50.check(exists)
def test_approved():
    """input age 30 and license yes yields RENTAL APPROVED"""
    result = (
        check50.run("python3 rental.py")
        .stdin("30", prompt=True)
        .stdin("yes", prompt=True)
        .stdout()
        .strip()
    )
    if result != "RENTAL APPROVED":
        help = "Be sure to print RENTAL APPROVED only when age ≥ 26 and license is yes."
        raise check50.Mismatch("RENTAL APPROVED", result, help=help)


@check50.check(exists)
def test_rejected():
    """input age 27 and license no yields RENTAL REJECTED"""
    result = (
        check50.run("python3 rental.py")
        .stdin("27", prompt=True)
        .stdin("no", prompt=True)
        .stdout()
        .strip()
    )
    if result != "RENTAL REJECTED":
        help = "If the user is 26+ but has no license, print RENTAL REJECTED."
        raise check50.Mismatch("RENTAL REJECTED", result, help=help)


@check50.check(exists)
def test_denied():
    """input age 20 and license yes yields RENTAL DENIED"""
    result = (
        check50.run("python3 rental.py")
        .stdin("20", prompt=True)
        .stdin("yes", prompt=True)
        .stdout()
        .strip()
    )
    if result != "RENTAL DENIED":
        help = "Anyone under 26 should print RENTAL DENIED."
        raise check50.Mismatch("RENTAL DENIED", result, help=help)
