import check50

@check50.check()
def exists():
    """pyramid.py exists"""
    check50.exists("pyramid.py")

@check50.check(exists)
import check50

@check50.check()
def exists():
    """pyramid.py exists"""
    check50.exists("pyramid.py")

@check50.check(exists)
def test_volume_integer():
    """input of 4, 6, 9 yields output of 72.00"""
    check50.run("python3 pyramid.py")\
        .stdin("4", prompt=False)\
        .stdin("6", prompt=False)\
        .stdin("9", prompt=False)\
        .stdout("Volume: 72.00\n", regex=False)\
        .exit(0)

@check50.check(exists)
def test_volume_float():
    """input of 3, 5, 7.5 yields output of 37.50"""
    check50.run("python3 pyramid.py")\
        .stdin("3", prompt=False)\
        .stdin("5", prompt=False)\
        .stdin("7.5", prompt=False)\
        .stdout("Volume: 37.50\n", regex=False)\
        .exit(0)

@check50.check(exists)
def test_volume_decimal():
    """input of 4.25, 6.75, 9.1 yields output of 86.84"""
    check50.run("python3 pyramid.py")\
        .stdin("4.25", prompt=False)\
        .stdin("6.75", prompt=False)\
        .stdin("9.1", prompt=False)\
        .stdout("Volume: 87.02\n", regex=False)\
        .exit(0)

