print("Reading file content:")
try:
    with open("sample.txt", "rt") as fh:
        print(f"Line 1: {fh.readline()}")
        print(f"Line 2: {fh.readline()}")
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")