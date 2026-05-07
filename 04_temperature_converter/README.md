# Temperature Converter

Converts Fahrenheit temperatures to Celsius or Kelvin with input validation.

## Files
- `convert_temp.py` - Temperature conversion utility
- `grading_convert_temp.py` - Graded/reference version

## Description
This program:
- Takes Fahrenheit temperature as input
- Validates input (must be >= -459.67)
- Converts to Celsius or Kelvin based on user choice
- Uses functions for modular code design

## How to Run
```bash
python convert_temp.py
```

## Usage
```
Enter a Fahrenheit temperature: 32
Convert to k (for Kelvin) or c (for Celsius): c
32.0F = 0.0C
```

## Conversion Formulas
- Celsius: (F - 32) × 5/9
- Kelvin: (F - 32) × 5/9 + 273.15
