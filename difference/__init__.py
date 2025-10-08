import check50

@check50.check()
def exists():
    """difference.py exists"""
    check50.exists("difference.py")

@check50.check(exists)
def test_diff_positive():
    """input of 10 and 4 yields output of 6"""
    check50.run("python3 difference.py").stdin("10", prompt=False).stdin("4", prompt=False).stdout("6\n", regex=False).exit(0)

@check50.check(exists)
def test_diff_negative():
    """input of 3 and 9 yields output of -6"""
    check50.run("python3 difference.py").stdin("3", prompt=False).stdin("9", prompt=False).stdout("-6\n", regex=False).exit(0)
