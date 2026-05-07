# Expense Tracker

Tracks and categorizes personal expenses with persistent storage.

## Files
- `spendingTracker.py` - Expense tracking application
- `expenses.txt` - Data file with expense records

## Description
This application:
- Records expenses with item, amount, and category
- Categorizes spending (housing, food, transportation, etc.)
- Calculates total expenses and income
- Provides spending summaries by category
- Persists data to file between sessions
- Supports add and summarize operations

## How to Run
```bash
python spendingTracker.py
```

## Data Format
Expenses are stored as: `item,amount,category`

Example:
```
Apartment rent,1500.00,housing
Groceries,75.50,food
Gas,45.00,transportation
```

## Operations
- **summarize**: View total income, expenses by category, and remaining balance
- **add**: Add new expense entry
- **done**: Save and exit

## Features
- Input validation
- Category-based summarization
- Income and expense tracking
- Automatic file persistence
