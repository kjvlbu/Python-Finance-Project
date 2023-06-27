import csv
from datetime import datetime

def record_expense():

    while 1:
        try:
           amount = float(input("Please input the amount spent. "))
           category = str(input("Please enter the category of the expense. "))
           date = datetime.now().strftime("%d-%m-%Y")

           with open("expenses.csv", "a",) as file:
               writer = csv.writer(file)
               writer.writerow([date, amount, category])

           print("\nExpense saved successfully as expenses.csv!")
           return
        except ValueError:
            print("Please enter a valid input")

def display_expense():
    with open("expenses.csv", "r") as file:
        reader = csv.reader(file)
        data = False

        for row in reader:
            if len(row) == 3:
                data = True
                print(f"\nDate: {row[0]}, Amount: ${row[1]}, Category: {row[2]}")

        if not data:
            print("\nNo data found.")

def remove_expense():
    with open("expenses.csv", "w") as file:
        file.truncate()

    print("\nFile successfully wiped!")


def main():
    while 1:
        print("\nFinancial Expense Tracker 9000\n"
              "==============================")
        print("1. Record Expense")
        print("2. View Expenses")
        print("3. Delete All Expenses")
        print("4. Exit Application")

        choice = int(input("What do you want to do? (1-4): "))

        if choice == 1:
            record_expense()
        elif choice == 2:
            display_expense()
        elif choice == 3:
            remove_expense()
        elif choice == 4:
            print("\nShutting Down")
            break

if __name__ == '__main__':
    main()