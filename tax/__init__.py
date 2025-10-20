@check50.check(exists)
def test_whole_dollar():
    """input of $12.00 yields output of Sales tax: $1.23"""
    check50.run("python3 tax.py") \
        .stdout("Enter item price: ") \
        .stdin("$12.00") \
        .stdout("Sales tax: $1.23\n") \
        .exit()

@check50.check(exists)
def test_cents():
    """input of $3.50 yields output of Sales tax: $0.36"""
    check50.run("python3 tax.py") \
        .stdout("Enter item price: ") \
        .stdin("$3.50") \
        .stdout("Sales tax: $0.36\n") \
        .exit()

@check50.check(exists)
def test_large_price():
    """input of $99.99 yields output of Sales tax: $10.25"""
    check50.run("python3 tax.py") \
        .stdout("Enter item price: ") \
        .stdin("$99.99") \
        .stdout("Sales tax: $10.25\n") \
        .exit()
