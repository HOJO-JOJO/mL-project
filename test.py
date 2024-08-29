import os
import json
from datetime import datetime

class FinanceManager:
    def __init__(self, data_file='data.txt'):
        self.data_file = data_file
        self.transactions = self.load_data()
    
    def load_data(self):
        if not os.path.exists(self.data_file):
            return {'income': [], 'expenses': []}
        with open(self.data_file, 'r') as file:
            return json.load(file)
    
    def save_data(self):
        with open(self.data_file, 'w') as file:
            json.dump(self.transactions, file, indent=4)
    
    def add_transaction(self, amount, category, date, transaction_type):
        transaction = {
            'amount': amount,
            'category': category,
            'date': date
        }
        if transaction_type == 'income':
            self.transactions['income'].append(transaction)
        elif transaction_type == 'expense':
            self.transactions['expenses'].append(transaction)
        self.save_data()
    
    def view_summary(self):
        total_income = sum(t['amount'] for t in self.transactions['income'])
        total_expenses = sum(t['amount'] for t in self.transactions['expenses'])
        savings = total_income - total_expenses
        
        print(f"Total Income: ${total_income:.2f}")
        print(f"Total Expenses: ${total_expenses:.2f}")
        print(f"Savings: ${savings:.2f}")
    
    def generate_report(self):
        report = "Income and Expenses Report\n"
        report += "="*30 + "\n"
        
        report += "Income:\n"
        for item in self.transactions['income']:
            report += f"  {item['date']}: ${item['amount']} - {item['category']}\n"
        
        report += "\nExpenses:\n"
        for item in self.transactions['expenses']:
            report += f"  {item['date']}: ${item['amount']} - {item['category']}\n"
        
        print(report)
    
def main():
    fm = FinanceManager()
    
    while True:
        print("\nPersonal Finance Manager")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Generate Report")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '1':
            amount = float(input("Enter income amount: "))
            category = input("Enter income category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            fm.add_transaction(amount, category, date, 'income')
        
        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter expense category: ")
            date = input("Enter date (YYYY-MM-DD): ")
            fm.add_transaction(amount, category, date, 'expense')
        
        elif choice == '3':
            fm.view_summary()
        
        elif choice == '4':
            fm.generate_report()
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice, please try again.")
    
if __name__ == "__main__":
    main()
