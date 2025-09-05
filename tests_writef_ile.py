from functions.write_file import write_file

def test_main():
    result = run_python_file("calculator", "main.py")
    print(result)

def test_calc():
    run_python_file("calculator", "main.py", ["3 + 5"])
    print(result)

def test_tests():
    run_python_file("calculator", "tests.py")
    print(result)

def test_error():
    run_python_file("calculator", "../main.py")
    print(result)

def test_nonexistent():
    run_python_file("calculator", "nonexistent.py")
    print(result)

if __name__ == "__main__":
    test_write_lorem()
    test_write_morelorem()
    test_write_outside()
