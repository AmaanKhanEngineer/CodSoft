import random
import string

def generate_password(length):
    # Define the possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive integer.")
                continue
            password = generate_password(length)
            print(f"Generated Password: {password}")
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
