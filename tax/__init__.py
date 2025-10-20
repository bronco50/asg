import check50
from re import escape


@check50.check()
def exists():
    """tax.py exists"""
    check50.exists("tax.py")


@check50.check(exists)
def test_whole_dollar():
    """input of $12.00 yields correct formatted output"""
    inputs = ["$12.00"]
    output = "Enter item price: $12.00Sales tax: $1.23\n"
    check50.run("python3 tax.py")\
        .stdin(inputs[0], prompt=False)\
        .stdout(regex(output), output, regex=True)\
        .exit(0)


@check50.check(exists)
def test_cents():
    """input of $3.50 yields correct formatted output"""
    inputs = ["$3.50"]
    output = "Enter item price: $3.50Sales tax: $0.36\n"
    check50.run("python3 tax.py")\
        .stdin(inputs[0], prompt=False)\
        .stdout(regex(output), output, regex=True)\
        .exit(0)


@check50.check(exists)
def test_large_price():
    """input of $99.99 yields correct formatted output"""
    inputs = ["$99.99"]
    output = "Enter item price: $99.99Sales tax: $10.25\n"
    check50.run("python3 tax.py")\
        .stdin(inputs[0], prompt=False)\
        .stdout(regex(output), output, regex=True)\
        .exit(0)


@check50.check(exists)
def test_small_price():
    """input of $1.00 yields correct formatted output"""
    inputs = ["$1.00"]
    output = "Enter item price: $1.00Sales tax: $0.10\n"
    check50.run("python3 tax.py")\
        .stdin(inputs[0], prompt=False)\
        .stdout(regex(output), output, regex=True)\
        .exit(0)


@check50.check(exists)
def test_rounding():
    """input of $5.55 yields correctly rounded formatted output"""
    inputs = ["$5.55"]
    output = "Enter item price: $5.55Sales tax: $0.57\n"
    check50.run("python3 tax.py")\
        .stdin(inputs[0], prompt=False)\
        .stdout(regex(output), output, regex=True)\
        .exit(0)


def regex(text):
    """match case-sensitively with any characters preceding and only whitespace after"""
    return fr'^.*{escape(text)}\s*$'
