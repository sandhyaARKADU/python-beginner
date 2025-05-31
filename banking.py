def show_balence():
    print(f"Your balance is ${balance:.2f}")


def deposit():
    amount = float(input("Enter an amount to be deposited:"))

    if amount < 0:
        print("That's not a amount")
        return 0
    else:

        return amount

def withdraw():
    amount = float(input("Enter an amount to be withdrawn:"))
    if amount > balance:
        print("Insufficient balance")
        return 0
    elif amount < 0:
        print("Amount must be greater then 0")
        return 0
    else:
        return amount

    
    

balance = 0
is_running = True

while is_running:
    print("1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        show_balence()
    elif choice == '2':
         balance += deposit()
    elif choice == '3':
       balance -= withdraw()
    elif choice == '4':
        is_running = False
    else:
        print("Invalid choice. Please try again.")

        print("Thank you! have a nice day!")
