balance = 1000000

while True:
    print("\n===== ATM MENU =====")
    print("1. Accent value")
    print("2. Take Money")
    print("3. Get money")
    print("4. Exit")

    choice = input(" choice: ")

    if choice == "1":
        print(" Your value:", balance, "$")

    elif choice == "2":
        amount = int(input(" Enter Number you want take : "))

        if amount <= 0:
            print(" Not Valid")

        elif amount > balance:
            print(" no kafi Money")

        else:
            balance -= amount
            print(" Secsses !")
            print(" Your Value:", balance)

    elif choice == "3":
        amount = int(input("Enter Number you want get : "))

        if amount > 0:
            balance += amount
            print(" Secsses ! ")
            print(" Your Value: ", balance)
        else:
            print(" Not Valid ")

    elif choice == "4":
        print(" Goodbye ! ")
        break

    else:
        print("choose aneother...")
