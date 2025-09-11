💰 Personal Finance Manager
Take control of your money — simply, locally, and securely. 

A lightweight, Python-based command-line application to help you track income, expenses, and savings — all stored locally in a plain text file. No databases, no cloud, no fuss.

🌟 Features
✅ Add Income — Log your earnings with amount, category, and date.
✅ Add Expense — Track where your money goes with customizable categories.
✅ View Summary — Instantly see total income, expenses, and net savings.
✅ Generate Report — Get a detailed, date-sorted breakdown of all transactions.
✅ Data Persistence — All records saved to data.txt (auto-created if missing).
✅ Zero Dependencies — Built with Python’s standard library. Runs anywhere!

🚀 Installation
1. Clone the Repository
bash


1
git clone https://github.com/yourusername/finance-manager.git
2. Navigate to Project Directory
bash


1
cd finance-manager
✅ No external libraries needed — pure Python! 

🖥️ Usage
Run the application:

bash


1
python finance_manager.py
Follow the interactive menu to:

➕ Add Income or Expense
📊 View Financial Summary
📄 Generate Detailed Transaction Report
📁 File Management
All your financial data is stored in:



1
data.txt
⚠️ Important: Do not delete this file — it contains all your transaction history! 

🧱 Code Structure
FinanceManager Class
__init__(data_file)
Initializes manager & loads data from file.
load_data()
Reads existing transactions from
data.txt
.
save_data()
Saves current transactions back to file.
add_transaction(...)
Adds income/expense with amount, category, date.
view_summary()
Displays totals for income, expenses, and savings.
generate_report()
Prints full categorized transaction history.

main() Function
Provides the interactive CLI menu for user actions.

🤝 Contributions
We ❤️ contributions! Here’s how to help:

🍴 Fork the repository
🌿 Create your feature branch (git checkout -b feature/AmazingFeature)
🛠️ Commit your changes (git commit -m 'Add some AmazingFeature')
🚀 Push to the branch (git push origin feature/AmazingFeature)
📬 Open a Pull Request
📜 License
Distributed under the MIT License. See LICENSE for details.

📬 Contact
Have questions, feedback, or feature requests?

➡️ Open an Issue on GitHub.

💡 Simple tools for simple finances — because managing money shouldn’t be complicated. 

