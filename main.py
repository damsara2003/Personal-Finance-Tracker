import json

# Global list to store transactions
transactions = []

# File handling functions
def load_transactions():
    try:
        with open("transactions.json", "r") as file:
            global transactions
            transactions = json.load(file)
    except FileNotFoundError:
        print("No existing transactions file found. Starting with an empty list.")

def save_transactions():
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=2)

# Feature implementations
def add_transaction():
    # Placeholder for adding a transaction logic
    amount = float(input("Enter the amount: "))
    category = input("Enter the category: ")
    transaction_type = input("Enter the type (Income/Expense): ")
    date = input("Enter the date (YYYY-MM-DD): ")

    transaction = [amount, category, transaction_type, date]
    transactions.append(transaction)

    save_transactions()
    print("Transaction added successfully.")

def view_transactions():
    # Placeholder for viewing transactions logic
    for index, transaction in enumerate(transactions, 1):
        print(f"{index}. Amount: {transaction[0]}, Category: {transaction[1]}, Type: {transaction[2]}, Date: {transaction[3]}")

def update_transaction():
    # Placeholder for updating a transaction logic
    view_transactions()
    try:
        index = int(input("Enter the index of the transaction to update: ")) - 1
        if 0 <= index < len(transactions):
            amount = float(input("Enter the new amount: "))
            category = input("Enter the new category: ")
            transaction_type = input("Enter the new type (Income/Expense): ")
            date = input("Enter the new date (YYYY-MM-DD): ")

            transactions[index] = [amount, category, transaction_type, date]
            save_transactions()
            print("Transaction updated successfully.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def delete_transaction():
    # Placeholder for deleting a transaction logic
    view_transactions()
    try:
        index = int(input("Enter the index of the transaction to delete: ")) - 1
        if 0 <= index < len(transactions):
            del transactions[index]
            save_transactions()
            print("Transaction deleted successfully.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def display_summary():
    # Placeholder for summary display logic
    total_income = sum(transaction[0] for transaction in transactions if transaction[2] == "Income")
    total_expense = sum(transaction[0] for transaction in transactions if transaction[2] == "Expense")
    balance = total_income - total_expense

    print(f"\nSummary:")
    print(f"Total Income: {total_income}")
    print(f"Total Expense: {total_expense}")
    print(f"Balance: {balance}")

def main_menu():
    load_transactions()  # Load transactions at the start
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Update Transaction")
        print("4. Delete Transaction")
        print("5. Display Summary")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_transactions()
        elif choice == '3':
            update_transaction()
        elif choice == '4':
            delete_transaction()
        elif choice == '5':
            display_summary()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
