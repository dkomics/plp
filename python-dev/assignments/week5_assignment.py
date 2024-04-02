def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with some text and numbers: 67890\n")
        print("File 'my_file.txt' created successfully.")
    except PermissionError:
        print("Permission denied to create the file.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("File creation process completed.\n")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of 'my_file.txt':")
            print(file.read())
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to read the file.")
    except Exception as e:
        print("An error occurred:", e)

def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Additional line 1\n")
            file.write("Appending more content\n")
            file.write("This is the last line\n")
        print("\nAdditional content appended to 'my_file.txt'.")
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to append to the file.")
    except Exception as e:
        print("An error occurred:", e)

# Task 1: File Creation
create_file()

# Task 2: File Reading and Display
read_file()

# Task 3: File Appending
append_file()
