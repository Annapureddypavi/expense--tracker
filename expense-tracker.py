expenses = []


def add_expense():
    print("\n--- Add Expense ---")

    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")

    expense = {
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)

    print("Expense added successfully!")


def view_expenses():
    print("\n--- Expenses ---")

    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(
            f"{expense['description']} - "
            f"₹{expense['amount']:.2f} - "
            f"{expense['category']}"
        )


def total_expenses():
    total = 0

    for expense in expenses:
        total += expense["amount"]

    print(f"\nTotal Expenses: ₹{total:.2f}")


def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expenses()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
