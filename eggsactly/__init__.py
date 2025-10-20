import check50
from re import escape


@check50.check()
def exists():
    """eggsactly.py exists"""
    check50.exists("eggsactly.py")


@check50.check(exists)
def test_exact_carton():
    """input of 12 yields correct formatted output"""
    inputs = ["12"]
    output = "Eggs: Cartons: 1\nLeftover: 0\n"
    check50.run("python3 eggsactly.py")\
        .stdin(inputs[0], prompt=False)\
        .stdout(regex(output), output, regex=True)\
        .exit(0)


@check50.check(exists)
def test_partial_carton():
    """input of 25 yields correct formatted output"""
    inputs = ["25"]
    output = "Eggs: Cartons: 2\nLeftover: 1\n"
    check50.run("python3 eggsactly.py")\
        .stdin(inputs[0], prompt=False)\
        .stdout(regex(output), output, regex=True)\
        .exit(0)


@check50.check(exists)
def test_no_eggs():
    """input of 0 yields correct formatted output"""
    inputs = ["0"]
    output = "Eggs: Cartons: 0\nLeftover: 0\n"
    check50.run("python3 eggsactly.py")\
        .stdin(inputs[0], prompt=False)\
        .stdout(regex(output), output, regex=True)\
        .exit(0)


@check50.check(exists)
def test_less_than_carton():
    """input of 11 yields correct formatted output"""
    inputs = ["11"]
    output = "Eggs: Cartons: 0\nLeftover: 11\n"
    check50.run("python3 eggsactly.py")\
        .stdin(inputs[0], prompt=False)\
        .stdout(regex(output), output, regex=True)\
        .exit(0)


@check50.check(exists)
def test_multiple_cartons():
    """input of 48 yields correct formatted output"""
    inputs = ["48"]
    output = "Eggs: Cartons: 4\nLeftover: 0\n"
    check50.run("python3 eggsactly.py")\
        .stdin(inputs[0], prompt=False)\
        .stdout(regex(output), output, regex=True)\
        .exit(0)


def regex(text):
    """match case-sensitively with any characters preceding and only whitespace after"""
    return fr'^.*{escape(text)}\s*$'
