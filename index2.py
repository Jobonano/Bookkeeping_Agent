import json
import datetime

# Basic structure to store transactions
transactions = []

def get_expense_category(description):
    """
    Categorize an expense based on its description using simple keywords.
    """
    # Basic categorization logic based on keywords
    description = description.lower()
    if "office" in description or "supplies" in description:
        return 'Office Supplies'
    elif "movie" in description or "ticket" in description or "entertainment" in description:
        return 'Entertainment'
    elif "food" in description or "restaurant" in description or "grocery" in description:
        return 'Food'
    elif "electric" in description or "gas" in description or "water" in description:
        return 'Utilities'
    elif "transport" in description or "fuel" in description or "uber" in description:
        return 'Transport'
    else:
        return 'Other'

def add_transaction(amount, description, transaction_type):
    """
    Adds a transaction to the bookkeeping system, categorizing it locally.
    """
    category = get_expense_category(description)
    transaction = {
        "amount": amount,
        "description": description,
        "category": category,
        "type": transaction_type,  # "expense" or "income"
        "date": str(datetime.datetime.now().date())
    }
    transactions.append(transaction)
    return transaction

def generate_report():
    """
    Generate a simple report of transactions.
    """
    income_total = sum([t['amount'] for t in transactions if t['type'] == 'income'])
    expense_total = sum([t['amount'] for t in transactions if t['type'] == 'expense'])
    balance = income_total - expense_total

    report = {
        "total_income": income_total,
        "total_expenses": expense_total,
        "balance": balance,
        "transactions": transactions
    }
    return report

def print_report(report):
    """
    Print a user-friendly report
    """
    print("\n--- Bookkeeping Report ---")
    print(f"Total Income: ${report['total_income']:.2f}")
    print(f"Total Expenses: ${report['total_expenses']:.2f}")
    print(f"Balance: ${report['balance']:.2f}")
    
    print("\nTransactions:")
    for t in report['transactions']:
        print(f"{t['date']} - {t['description']} - {t['category']} - ${t['amount']:.2f} - {t['type']}")

def main():
    """
    Main loop to interact with the user for transactions and generate reports.
    """
    print("Welcome to your Bookkeeping AI Agent!")
    
    while True:
        print("\n1. Add transaction\n2. View report\n3. Exit")
        choice = input("Select an option (1/2/3): ")

        if choice == "1":
            # Input transaction details
            amount = float(input("Enter amount (positive for income, negative for expense): "))
            description = input("Enter description of the transaction: ")
            transaction_type = 'income' if amount > 0 else 'expense'
            
            transaction = add_transaction(amount, description, transaction_type)
            print(f"Transaction added: {transaction}")

        elif choice == "2":
            # Generate and print report
            report = generate_report()
            print_report(report)

        elif choice == "3":
            print("Exiting Bookkeeping AI Agent. Goodbye!")
            break

        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
