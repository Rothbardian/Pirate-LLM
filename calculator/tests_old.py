from functions.write_file import write_file

def test_write_lorem():
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)

def test_write_morelorem():
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)

def test_write_outside():
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)

if __name__ == "__main__":
    test_write_lorem()
    test_write_morelorem()
    test_write_outside()
