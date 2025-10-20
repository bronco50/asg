import check50
from re import escape

# Adds case-insensitive matching
case_insensitive_prefix = "(?i)"


@check50.check()
def exists():
    """name_box.py exists"""
    check50.exists("name_box.py")


@check50.check(exists)
def test_single_case():
    """formats full name correctly for 'Ada Lovelace'"""
    first = "Ada"
    last = "Lovelace"

    # Expected exact centered output
    output = (
        "+----------------+\n"
        "|  Lovelace, Ada  |\n"
        "+----------------+\n"
    )

    check50.run("python3 name_box.py")\
        .stdin(first, prompt=True)\
        .stdin(last, prompt=True)\
        .stdout(case_insensitive_prefix + escape(output), output, regex=True)\
        .exit()


# --------------------------------------------------------------------
# Hints (automatically shown when the check fails)
# --------------------------------------------------------------------
@check50.hint("Make sure to format the full name as '{last_name}, {first_name}' — include the comma and space.")
@check50.hint("Center the full name within the box using .center(width).")
@check50.hint("The width should be len(full_name) + 4 — two spaces and two borders.")
@check50.hint("Top and bottom borders must use '+' and '-' and match the exact width.")
@check50.hint("Do not add extra blank lines; your box should have exactly three lines.")
def hints():
    pass
