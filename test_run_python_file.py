from functions.run_python_file import run_python_file

def test() -> None:
    result = run_python_file("calculator", "main.py")
    print("Result for 'main.py' file: Produces usage information since no arguments are provided")
    print(result)
    print("")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result for 'main.py' with addition arguments:")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result for 'tests.py' file:")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Result for bad '../main.py' file: Error expected since it is outside the working directory")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result for 'nonexistent.py' nonexistent file: Error expected since it does not exist")
    print(result)
    print("")

    result = run_python_file("calculator", "lorem.txt")
    print("Result for 'lorem.txt' file: Error expected since it's not a Python file")
    print(result)


if __name__ == "__main__":
    test()
