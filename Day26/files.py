import os

# define function to display menu options
def display_menu():
    print("1. Create a new file")
    print("2. Open an existing file")
    print("3. Save the current file")
    print("4. Save the current file as a new file")
    print("5. Quit the program")

# define function to create a new file
def create_new_file():
    filename = input("Enter the filename: ")
    if os.path.exists(filename):
        print("Error: file already exists")
        return
    with open(filename, "w") as f:
        print(f"File {filename} created successfully")

# define function to open an existing file
def open_existing_file():
    filename = input("Enter the filename: ")
    if not os.path.exists(filename):
        print("Error: file does not exist")
        return
    with open(filename, "r") as f:
        contents = f.read()
        print(contents)

# define function to save the current file
def save_current_file(filename, contents):
    with open(filename, "w") as f:
        f.write(contents)
        print(f"File {filename} saved successfully")

# define function to save the current file as a new file
def save_current_file_as():
    new_filename = input("Enter the new filename: ")
    if os.path.exists(new_filename):
        print("Error: file already exists")
        return
    with open(current_filename, "r") as f:
        contents = f.read()
    with open(new_filename, "w") as f:
        f.write(contents)
        print(f"File {new_filename} saved successfully")

# main program loop
current_filename = ""
contents = ""
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        create_new_file()
        current_filename = filename
        contents = ""
    elif choice == "2":
        open_existing_file()
        current_filename = filename
        with open(filename, "r") as f:
            contents = f.read()
    elif choice == "3":
        if current_filename == "":
            print("Error: no file currently open")
        else:
            save_current_file(current_filename, contents)
    elif choice == "4":
        if current_filename == "":
            print("Error: no file currently open")
        else:
            save_current_file_as()
            current_filename = new_filename
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Error: invalid choice")
