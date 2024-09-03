bank_account = {
    1001: {
        "first_name": "Shilo",
        "last_name": "Shtral",
        "id_number": "207775958",
        "balance": 30000,
        "transactions_to_execute": [
            ("2024-08-17 14:00:00", 1001, 1002, 300),
            ("2024-08-17 15:00:00", 1001, 1003, 200)
        ],
        "transaction_history": [
            ("2024-08-15 09:00:00", 1001, 1002, 500),
            ("2024-08-15 09:30:00", 1001, 1003, 150)
        ]
    },
    1002: {
        "first_name": "Eli",
        "last_name": "Peretz",
        "id_number": "102030400",
        "balance": 15000,
        "transactions_to_execute": [
            ("2024-08-17 14:00:00", 1002, 1001, 300),
            ("2024-08-17 15:00:00", 1002, 1003, 200)
        ],
        "transaction_history": [
            ("2024-08-15 09:00:00", 1002, 1003, 500),
            ("2024-08-15 09:30:00", 1002, 1001, 150)
        ]
    },
    1003: {
        "first_name": "Yossi",
        "last_name": "Elbaz",
        "id_number": "908070605",
        "balance": 12000,
        "transactions_to_execute": [
            ("2024-08-17 14:00:00", 1003, 1002, 300),
            ("2024-08-17 15:00:00", 1003, 1001, 200)
        ],
        "transaction_history": [
            ("2024-08-15 09:00:00", 1003, 1002, 500),
            ("2024-08-15 09:30:00", 1003, 1001, 150)
        ]
    }
}

def process_transactions(account):
    transactions_to_execute = list(account["transactions_to_execute"])

    for transaction in transactions_to_execute:
        date, from_account, to_account, amount = transaction
        if bank_account[from_account]["balance"] >= amount:
            bank_account[from_account]["balance"] -= amount
            bank_account[to_account]["balance"] += amount

            from_history = list(bank_account[from_account]["transaction_history"])
            to_history = list(bank_account[to_account]["transaction_history"])

            from_history.append((date, from_account, to_account, -amount))
            to_history.append((date, from_account, to_account, amount))

            bank_account[from_account]["transaction_history"] = tuple(from_history)
            bank_account[to_account]["transaction_history"] = tuple(to_history)

            print(f"Processed transaction from account {from_account} to account {to_account} of amount {amount} on {date}")
        else:
            print(f"Insufficient balance in account {from_account} for transaction of amount {amount}.")

    account["transactions_to_execute"] = tuple()

def print_all_accounts():
    for account_number, details in bank_account.items():
        print(f"Account Number: {account_number}, Name: {details['first_name']} {details['last_name']}, ID: {details['id_number']}, Balance: {details['balance']}")

def find_account_by_number(account_number):
    account = bank_account.get(account_number)
    if account:
        print(f"Account Number: {account_number}, Name: {account['first_name']} {account['last_name']}, ID: {account['id_number']}, Balance: {account['balance']}")
    else:
        print(f"No account found with number {account_number}.")

def find_account_by_id_number(id_number):
    found = False
    for account_number, details in bank_account.items():
        if details["id_number"] == id_number:
            print(f"Account Number: {account_number}, Name: {details['first_name']} {details['last_name']}, ID: {details['id_number']}, Balance: {details['balance']}")
            found = True
    if not found:
        print(f"No account found with ID number {id_number}.")

def find_account_by_name(first_name):
    found = False
    first_name = first_name.lower()
    for account_number, details in bank_account.items():
        if first_name in details['first_name'].lower():
            print(f"Account Number: {account_number}, Name: {details['first_name']} {details['last_name']}, ID: {details['id_number']}, Balance: {details['balance']}")
            found = True
    if not found:
        print(f"No account found with first name containing '{first_name}'.")

def reports_menu():
    while True:
        print("\nReports Menu:")
        print("1. Print all bank accounts")
        print("2. Find and print a specific account by account number")
        print("3. Find account by ID number")
        print("4. Find account by first name")
        print("5. Go back to the previous menu")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            print_all_accounts()
        elif choice == "2":
            account_number = int(input("Enter the account number: "))
            find_account_by_number(account_number)
        elif choice == "3":
            id_number = input("Enter the ID number: ")
            find_account_by_id_number(id_number)
        elif choice == "4":
            first_name = input("Enter the first name: ")
            find_account_by_name(first_name)
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

def bank_app():
    while True:
        try:
            account_number = int(input("Enter your account number (or 0 for reports): "))
            if account_number == 0:
                reports_menu()
            elif account_number in bank_account:
                account = bank_account[account_number]
                first_name = account["first_name"]
                print(f"Hello {first_name}, what action would you like to perform?")

                while True:
                    print("\nChoose an action:")
                    print("1. Add a new transaction")
                    print("2. Process all current transactions")
                    print("3. Exit")

                    choice = input("Enter your choice (1, 2, or 3): ")

                    if choice == "1":
                        date = input("Enter the transaction date (YYYY-MM-DD HH:MM:SS): ")
                        from_account = int(input("Enter the from account number: "))
                        to_account = int(input("Enter the to account number: "))
                        amount = int(input("Enter the amount: "))

                        if from_account in bank_account and to_account in bank_account:
                            transactions = list(bank_account[from_account]["transactions_to_execute"])
                            transactions.append((date, from_account, to_account, amount))
                            bank_account[from_account]["transactions_to_execute"] = tuple(transactions)
                            print("Transaction added successfully.")
                        else:
                            print("One or both of the account numbers are incorrect.")

                    elif choice == '2':
                        process_transactions(account)
                        print("All current transactions have been processed.")

                    elif choice == '3':
                        print("Exiting...")
                        break

                    else:
                        print("Invalid choice, please try again.")
            else:
                print("You've entered a wrong bank account number! Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    bank_app()
