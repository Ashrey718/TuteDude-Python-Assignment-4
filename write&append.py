with open("output.txt","wt") as fh:
    fh.write(input("Enter text to write to the file: ")+"\n")
    print("Data successfully written to output.txt.")

with open("output.txt","at") as fh:
    fh.write(input("Enter additional text to append: "))
    print("Data successfully appended.")

with open("output.txt","rt") as fh:
    print("Final content of output.txt:")
    print(fh.read())