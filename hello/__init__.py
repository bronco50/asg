import check50

@check50.check()
def exists():
    """hello.py exists"""
    check50.exists("hello.py")

@check50.check(exists)
def prints_hello_bronco():
    """prints 'Hello, Bronco!'"""
    check50.run("python3 hello.py").stdout("Hello, Bronco!\n", regex=False).exit(0)
