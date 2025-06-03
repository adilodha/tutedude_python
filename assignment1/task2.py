# Write a Python program that:
# 1.  Takes a user's first name and last name as input.
# 2.  Concatenates the first name and last name into a full name.
# 3.  Prints a personalized greeting message using the full name.

def main(): 
    # Taking first name and last name as input from the user
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # Printing a personalized greeting message using the full name
    print(f"Hello, {first_name} {last_name}! Welcome to the Python program.")


if __name__ == "__main__":
    main()