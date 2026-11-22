import random
import string

while True:
    print("\n===== MAIN MENU =====")
    print("1. Password Generator")
    print("2. Number Guessing Game")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        length = int(input("Enter password length: "))

        characters = string.ascii_letters + string.digits + string.punctuation

        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Your password is:", password)

    elif choice == "2":
        
        secret_number = random.randint(1, 100)

        print("Guess a number between 1 and 100")
        print("You have 7 attempts.")

        for i in range(1, 8):

            guess = int(input(f"Attempt {i}: "))

            if guess == secret_number:
                print("Yes ! You won!")
                break

            elif guess < secret_number:
                print("Go Higher")

            else:
                print("Go Lower")

        else:
            print("Game Over")
            print("The correct number was:", secret_number)

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice!")
