expenses = []
budget = 5000.0


def add_expense():
    name = input("Enter item name: ")
    category = input("Enter category (Food/Travel/Study/Other): ")
    amount = float(input("Enter amount: "))
    expenses.append({"name": name, "category": category, "amount": amount})
    print("Expense added.")


def view_expenses():
    if not expenses:
        print("No expenses found.")
        return
    total = 0
    for i, item in enumerate(expenses, 1):
        print(i, item["name"], "-", item["category"], "- Rs.", item["amount"])
        total += item["amount"]
    print("Total Spent: Rs.", total)


def category_summary():
    if not expenses:
        print("No expenses found.")
        return
    summary = {}
    for item in expenses:
        cat = item["category"]
        summary[cat] = summary.get(cat, 0) + item["amount"]
    for cat, amt in summary.items():
        print(cat, ": Rs.", amt)
    highest = max(summary, key=summary.get)
    print("Highest Spending:", highest, "Rs.", summary[highest])


def check_budget():
    global budget
    choice = input("Change budget? (y/n): ")
    if choice.lower() == "y":
        budget = float(input("Enter new budget: "))
    total = sum(item["amount"] for item in expenses)
    print("Budget:", budget, "| Spent:", total)
    if total > budget:
        print("Alert: Budget exceeded by Rs.", total - budget)
    else:
        print("Remaining Budget: Rs.", budget - total)


while True:
    print("\n1. Add Expense  2. View Expenses  3. Category Summary  4. Check Budget  5. Exit")
    ch = input("Enter choice (1-5): ")
    if ch == "1":
        add_expense()
    elif ch == "2":
        view_expenses()
    elif ch == "3":
        category_summary()
    elif ch == "4":
        check_budget()
    elif ch == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
