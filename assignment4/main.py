

# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist

def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.readlines()
            for line in content:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




# Task 2: Write and Append Data to a File
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.
def write_and_append_file(file_name):
    try:
        user_input = input("Enter some text to write to the file: ")
        with open(file_name, 'w') as file:
            file.write(user_input + "\n")
        print(f"Data successfully written to {file_name}")

        additional_input = input("Enter additional text to append to the file: ")
        with open(file_name, 'a') as file:
            file.write(additional_input + "\n")
        print(f"Data successfully appended.")

        print(f"Final content of {file_name}:")
        read_file(file_name)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function to execute the tasks 
def main():
    # Task 1: Read a file
    file_name = "sample.txt"
    read_file(file_name)

    # Task 2: Write and append to a file
    file_name = "output.txt"
    write_and_append_file(file_name)

if __name__ == "__main__":
    main()
