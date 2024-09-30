balance = 0

def show_menu():
    print("Welcome to Jean-Baptiste Bank!")
    print("1. Check balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")


while True:
    show_menu()
    
    
    choice = input("Enter your choice: ")

    if choice == '1':
        print(f"Your balance is ${balance}")

        continu =input("Will that be all? Y or N").upper()
        if continu == 'N':
             continue
        if continu == 'Y':
             print("Have a nice day! :)")
             break
    elif choice == '2':
        deposit=float(input("How much money would you like to deposit? "))
        if deposit > 0:
            balance += deposit
            print(f"Deposit was  successful! New balance is ${balance}")
        elif deposit < 0:
            print("Cannot deposit a negative balance. Back to main menu.")
    elif choice == '3':
        withdrawal=float(input(f"How much money would you like to withdraw? "))
        if withdrawal <= balance and withdrawal >0:
                balance -= withdrawal
                print(f"")
        else:
             print(f"Insufficient funds. You only have ${balance} in your account")
        
    elif choice == '4':
        print("Have a nice day! :)")
        break


    


    #commenting


    