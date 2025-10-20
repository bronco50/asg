import check50


@check50.check()
def exists():
    """tax.py exists"""
    check50.exists("tax.py")


@check50.check(exists)
def test_whole_dollar():
    """input of $12.00 yields output of Sales tax: $1.23"""
    check50.run("python3 tax.py").stdin("$12.00", prompt=False).stdout(""Enter item price: $12.00/nSales tax: $1.23").exit()


@check50.check(exists)
def test_cents():
    """input of $3.50 yields output of Sales tax: $0.36"""
    check50.run("python3 tax.py").stdin("$3.50", prompt=False).stdout("Sales tax: $0.36").exit()


@check50.check(exists)
def test_large_price():
    """input of $99.99 yields output of Sales tax: $10.25"""
    check50.run("python3 tax.py").stdin("$99.99", prompt=False).stdout("Sales tax: $10.25").exit()


@check50.check(exists)
def test_small_price():
    """input of $1.00 yields output of Sales tax: $0.10"""
    check50.run("python3 tax.py").stdin("$1.00", prompt=False).stdout("Sales tax: $0.10").exit()


@check50.check(exists)
def test_rounding():
    """input of $5.55 yields output of Sales tax: $0.57"""
    check50.run("python3 tax.py").stdin("$5.55", prompt=False).stdout("Sales tax: $0.57").exit()
