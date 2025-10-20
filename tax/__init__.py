import check50


@check50.check()
def exists():
    """tax.py exists"""
    check50.exists("tax.py")


@check50.check(exists)
def test_whole_dollar():
    """input of $12.00 yields output of Sales tax: $1.23"""
    check50.run("python3 tax.py").stdin("$12.00", prompt=False).stdout("Sales tax: $1.23\n").exit()


@check50.check(exists)
def test_cents():
    """input of $3.50 yields output of Sales tax: $0.36"""
    check50.run("python3 tax.py").stdin("$3.50", prompt=False).stdout("Sales tax: $0.36\n").exit()


@check50.check(exists)
def test_large_price():
    """input of $99.99 yields output of Sales tax: $10.25"""
    check50.run("python3 tax.py").stdin("$99.99", prompt=False).stdout("Sales tax: $10.25\n").exit()


@check50.check(exists)
def test_small_price():
    """input of $1.00 yields output of Sales tax: $0.10"""
    check50.run("python3 tax.py").stdin("$1.00", prompt=False)
