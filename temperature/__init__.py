import check50

@check50.check()
def exists():
    """temperature.py exists"""
    check50.exists("temperature.py")

@check50.check(exists)
def converts_10c():
    """input of 10 yields output of 50.0"""
    check50.run("python3 temperature.py").stdin("10", prompt=False).stdout("50.0\n", regex=False).exit(0)

@check50.check(exists)
def converts_negative():
    """input of -40 yields output of -40.0"""
    check50.run("python3 temperature.py").stdin("-40", prompt=False).stdout("-40.0\n", regex=False).exit(0)

@check50.check(exists)
def converts_zero():
    """input of 0 yields output of 32.0"""
    check50.run("python3 temperature.py").stdin("0", prompt=False).stdout("32.0\n", regex=False).exit(0)
