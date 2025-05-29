try:
    with open("sample.txt", "r") as file:
        print("Contents of sample.txt:\n")
        for line in file:
            print(line.strip())  
    print("Error: The file 'sample.txt' does not exist.")


user_input = input("Enter some text to write to output.txt: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")
with open("output.txt", "a") as file:
    file.write("This is appended data.\n")
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
