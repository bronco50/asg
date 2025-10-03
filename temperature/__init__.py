import check50

@check50.check()
def exists():
    """temperature.py exists"""
    check50.exists("temperature.py")

@check50.check(exists)
def converts_10c():
    """converts 10°C to 50.0°F"""
    check50.run("python3 temperature.py").stdin("10").stdout("50.0").exit(0)

@check50.check(exists)
def converts_negative():
    """converts -40°C to -40.0°F"""
    check50.run("python3 temperature.py").stdin("-40").stdout("-40.0").exit(0)

@check50.check(exists)
def converts_zero():
    """converts 0°C to 32.0°F"""
    check50.run("python3 temperature.py").stdin("0").stdout("32.0").exit(0)
