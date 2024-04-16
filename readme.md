## Personal Finance Tracker 2.0

This is a Python application designed to help you manage your personal finances effectively. It allows you to track income and expenses, categorize transactions, view summaries, and import data in bulk.

**Features:**

* **Transaction Management:**
    * Add new transactions with purpose, amount, type (income/expense), and date.
    * View all existing transactions categorized by purpose.
    * Update existing transactions (amount, type, or date).
    * Delete transactions (all transactions under a purpose or a single transaction).
* **Data Storage:**
    * Transactions are stored persistently in a JSON file (`data.json`).
    * Error handling ensures the program gracefully handles missing or corrupt data files.
* **Summary Reports:**
    * Calculate and display total income, total expense, number of income transactions, number of expense transactions, and net value (total income minus total expense).
* **Bulk Import:**
    * Import transactions from a file in a specific format to add them to your existing data.

**Getting Started:**

1. **Requirements:**
    * Python 3 (tested with version 3.x)
2. **Running the Script:**
    * Save the script as `personal_finance_tracker.py`.
    * Open a terminal or command prompt and navigate to the directory containing the script.
    * Run the script using the following command: `python personal_finance_tracker.py`

**Using the Tracker:**

The program will display a menu with options for adding, viewing, updating, deleting transactions, displaying summary, reading bulk transactions, and exiting. Use the corresponding numbers (1-7) to select your desired action.

**Data File:**

The program uses a JSON file (`data.json`) to store your transaction data. This file is automatically created if it doesn't exist when you run the program. 

**Exiting the Program:**

When you're finished using the tracker, select option 7 (Exit) from the menu. The program will save your data to the JSON file and exit.

**Additional Notes:**

* The code includes input validation for amount and transaction type to ensure data integrity.
* Bulk import functionality allows you to easily add a large number of transactions from another source.
* Feel free to explore the Python script (`personal_finance_tracker.py`) to understand the code's logic and potentially customize it further based on your needs.

We hope this Personal Finance Tracker 2.0 helps you manage your finances effectively!