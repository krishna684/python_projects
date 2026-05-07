# Shopping Calculator

Calculates total shopping costs from a price list.

## Files
- `shopping.py` - Shopping calculator utility
- `prices.txt` - Product prices in CSV format

## Description
This program:
- Reads product prices from a text file
- Validates price data format and values
- Calculates total shopping cost
- Supports cleaning/validation of price data
- Handles malformed entries gracefully

## How to Run
```bash
python shopping.py
```

## Price File Format
```
item_name,price
apple,1.50
milk,3.99
bread,2.50
```

## Features
- Input validation
- Error handling for invalid prices
- Calculates running total
- Cleans and validates input data
