import check50
from re import escape

# adds case insensitivity
case_insensitive_prefix = "(?i)"


@check50.check()
def exists():
    """eggsactly.py exists"""
    check50.exists("eggsactly.py")


@check50.check(exists)
def test_normal_case():
    """input of 24 yields Cartons: 2 and Leftover: 0"""
    input_val = "24"
    output = "Cartons: 2\nLeftover: 0\n"
    check50.run("python3 eggsactly.py")\
        .stdin(input_val, prompt=True)\
        .stdout(case_insensitive_prefix + escape(output), output, regex=True)\
        .exit()


@check50.check(exists)
def test_zero_eggs():
    """input of 0 yields Cartons: 0 and Leftover: 0"""
    input_val = "0"
    output = "Cartons: 0\nLeftover: 0\n"
    check50.run("python3 eggsactly.py")\
        .stdin(input_val, prompt=True)\
        .stdout(case_insensitive_prefix + escape(output), output, regex=True)\
        .exit()


@check50.check(exists)
def test_one_leftover():
    """input of 25 yields Cartons: 2 and Leftover: 1"""
    input_val = "25"
    output = "Cartons: 2\nLeftover: 1\n"
    check50.run("python3 eggsactly.py")\
        .stdin(input_val, prompt=True)\
        .stdout(case_insensitive_prefix + escape(output), output, regex=True)\
        .exit()
