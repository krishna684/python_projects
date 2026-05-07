# Budget Planner

Calculates monthly budget based on historical expense data with sinking fund allocation.

## Files
- `budgetPlanner.py` - Main budget calculation application
- `jan_expenses.txt` - January expense records
- `feb_expenses.txt` - February expense records
- `mar_expenses.txt` - March expense records
- `apr_expenses.txt` - April expense records
- `may_expenses.txt` - May expense records

## Description
This final project application:
- Analyzes historical expenses across selected months
- Calculates regular budget for recurring expense categories
- Identifies and budgets for sinking fund categories
- Provides comprehensive budget planning report

## How to Run
```bash
python budgetPlanner.py
```

## Usage Example
```
Which months' expenses should be used to plan the budget: jan,feb,mar
Based on the analysis of your expenses for the selected months, your budget is calculated as follows:
housing: $1055.18
dining out: $60.82
grocery: $54.00
... (more categories)

Finally, you should leave $29.97 as sinking fund for occasional spending, such as things in the categories of:
    medical
    study
```

## Budget Calculation

### Regular Categories
Categories appearing in 2+ selected months:
- Budget = Total amount across months ÷ Number of months

### Sinking Fund Categories  
Categories appearing in only 1 month:
- Sinking Fund = Total of all single-month categories ÷ Number of months

## Expense File Format
Each line: `item_description,amount,category`

Example:
```
Rent,1050.00,housing
Groceries,45.00,grocery
Movie,15.00,dining out
Personal items,30.00,personal
```

## Features
- Input validation with helpful error messages
- Invalid month detection
- Minimum 2-month requirement check
- Duplicate month prevention
- Clean, readable budget output
- Proper categorization of regular vs. sinking fund expenses
