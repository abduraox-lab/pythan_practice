expenses = [ ]
while True:
    print("\n---EXPENSE TRACKER---")
    print("1. Add Expense")
    print("2. View Expense")
    print("3. Search by cateogory")
    print("4. Delete Expense")
    print("5. Total Spending")
    print("6. Exit")

    choices = input("Enter your choices: ")
    if choices == "1":
        amount = float(input("Enter Amount: "))
        category = input("Enter category: ")
        description = input("Enter Description: ")
        expense = {"amount": amount,
                    "category": category,
                    "description": description}
        expenses.append(expense)
        print("Expense added succesfully!")

    elif choices == "2":
        if not expense:
            print("No expense found")
        else:
            print("\n---ALL EXPENSES---")
            for expense in expenses:
                print("Amount:", expense["amount"])
                print("category:", expense["category"])
                print("Description:", expense["description"])
                print("-------------------------------------")
    elif choices == "3":
        search_category = input("Enter category to search: ").lower()
        found = False
        for expense in expenses:
            if expense["category"].lower() == search_category:
                print("Amount:", expense["amount"])
                print("category:", expense["category"])
                print("Description:", expense["description"])
                print("-------------------------------------")
                found = True
                if not found:
                    print("No expense found in this category")
    elif choice == "4":
        if not expenses:
            print("No expenses found")
        else:
            print("\n---EXPENSES---")
            for index, expense in enumerate(expenses, start=1):
                print(index, expense["category"], "-", expense["amount"])
                delete_number = int(input("Enter expense number to delete: "))

                if 1 <= delete_number <= len(expenses):
                    delete_expense = expense.pop(delete_number - 1)
                    print("Expense deleted ok!")
                else:
                    print("Invalid expense number")

    elif choices == "5":
        if not expenses:
            print("No expenses found")
        else:
            total = 0
            for expense in expenses:
                total += expense["amount"]
                print("Total spending: $", total)

    elif choices == "6":
        print("Thank you for using Expense tracker!")
        break
    else:
        print("Invalid choice. please enter 1 to 6.")
            