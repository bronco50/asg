import check50

@check50.check()
def exists():
    """pyramid.py exists"""
    check50.exists("pyramid.py")

@check50.check(exists)
def test_volume_integer():
    """input of 4, 6, 9 yields output of 72.0"""
    check50.run("python3 pyramid.py")\
        .stdin("4", prompt=False)\
        .stdin("6", prompt=False)\
        .stdin("9", prompt=False)\
        .stdout("72.0\n", regex=False)\
        .exit(0)

@check50.check(exists)
def test_volume_float():
    """input of 3, 5, 7.5 yields output of 37.5"""
    check50.run("python3 pyramid.py")\
        .stdin("3", prompt=False)\
        .stdin("5", prompt=False)\
        .stdin("7.5", prompt=False)\
        .stdout("37.5\n", regex=False)\
        .exit(0)
