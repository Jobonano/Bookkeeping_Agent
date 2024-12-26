# Bookkeeping AI Agent

A simple Python-based bookkeeping system that helps users track their income and expenses. This command-line application allows for easy transaction management with automatic categorization and report generation capabilities.

## Features

- Add income and expense transactions
- Automatic categorization of expenses based on description keywords
- Generate detailed financial reports
- Track running balance
- Simple command-line interface
- Transaction date tracking

## Installation

Clone this repository:
```bash
git clone https://github.com/jobonano/Finance_Agent
cd Finance_Agent
```

No additional dependencies are required beyond Python's standard library.

## Usage

Run the program:
```bash
python index.py
```

The program offers three main options:
1. Add transaction
2. View report
3. Exit

### Adding Transactions

When adding a transaction:
- Enter a positive amount for income
- Enter a negative amount for expenses
- Provide a description for automatic categorization

Example:
```python
Select an option (1/2/3): 1
Enter amount (positive for income, negative for expense): -50.00
Enter description of the transaction: grocery shopping
```

### Expense Categories

The system automatically categorizes expenses into:
- Office Supplies
- Entertainment
- Food
- Utilities
- Transport
- Other

Categorization is based on keywords in the transaction description.

### Viewing Reports

Reports include:
- Total income
- Total expenses
- Current balance
- Detailed transaction list with dates, descriptions, categories, and amounts

Example report output:
```
--- Bookkeeping Report ---
Total Income: $1000.00
Total Expenses: $350.00
Balance: $650.00

Transactions:
2024-12-26 - salary deposit - Other - $1000.00 - income
2024-12-26 - grocery shopping - Food - $-50.00 - expense
```

## Code Structure

- `get_expense_category()`: Categorizes transactions based on description keywords
- `add_transaction()`: Records new transactions with metadata
- `generate_report()`: Creates financial summary and transaction list
- `print_report()`: Displays formatted report
- `main()`: Handles user interaction and program flow

## Data Storage

Transactions are currently stored in memory. The data structure for each transaction:
```python
{
    "amount": float,
    "description": str,
    "category": str,
    "type": str,  # "expense" or "income"
    "date": str
}
```

## Future Improvements

Potential enhancements could include:
- Persistent storage (database or file-based)
- Custom category management
- Date range filtering for reports
- Data export capabilities
- Budget tracking and alerts
- Multiple currency support

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
