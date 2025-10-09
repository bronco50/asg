import check50
from re import escape


@check50.check()
def exists():
    """pyramid.py exists"""
    check50.exists("pyramid.py")


@check50.check(exists)
def test_integer_values():
    """input of 4, 6, and 9 yields correct formatted output"""
    inputs = ["4", "6", "9"]
    output = "Enter base length: Enter base width: Enter height: Volume: 72.00\n"
    check50.run("python3 pyramid.py")\
        .stdin(inputs[0], prompt=False)\
        .stdin(inputs[1], prompt=False)\
        .stdin(inputs[2], prompt=False)\
        .stdout(regex(output), output, regex=True)\
        .exit(0)


@check50.check(exists)
def test_float_values():
    """input of 3, 5, and 7.5 yields correct formatted output"""
    inputs = ["3", "5", "7.5"]
    output = "Enter base length: Enter base width: Enter height: Volume: 37.50\n"
    check50.run("python3 pyramid.py")\
        .stdin(inputs[0], prompt=False)\
        .stdin(inputs[1], prompt=False)\
        .stdin(inputs[2], prompt=False)\
        .stdout(regex(output), output, regex=True)\
        .exit(0)


def regex(text):
    """match case-sensitively with any characters preceding and only whitespace after"""
    return fr'^.*{escape(text)}\s*$'
