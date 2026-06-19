expenses = []

def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\nExpenses:")
    for expense in expenses:
        print(expense["category"], ":", expense["amount"])

def total_expense():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("Total Expense =", total)

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expense()

    elif choice == "4":
        break

    else:
        print("Invalid choice!")
