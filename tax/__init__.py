import check50
from re import escape

# adds case insensitivity
case_insensitive_prefix = "(?i)"


@check50.check()
def exists():
    """tax.py exists"""
    check50.exists("tax.py")


@check50.check(exists)
def test_large_price():
    """input of $99.99 yields output of Sales tax: $10.25"""
    input_val = "$99.99"
    output = "Sales tax: $10.25\n"
    check50.run("python3 tax.py")\
        .stdin(input_val, prompt=True)\
        .stdout(case_insensitive_prefix + escape(output), output, regex=True)\
        .exit()


@check50.check(exists)
def test_small_price():
    """input of $1.00 yields output of Sales tax: $0.10"""
    input_val = "$1.00"
    output = "Sales tax: $0.10\n"
    check50.run("python3 tax.py")\
        .stdin(input_val, prompt=True)\
        .stdout(case_insensitive_prefix + escape(output), output, regex=True)\
        .exit()


@check50.check(exists)
def test_rounding():
    """input of $5.55 yields output of Sales tax: $0.57"""
    input_val = "$5.55"
    output = "Sales tax: $0.57\n"
    check50.run("python3 tax.py")\
        .stdin(input_val, prompt=True)\
        .stdout(case_insensitive_prefix + escape(output), output, regex=True)\
        .exit()
