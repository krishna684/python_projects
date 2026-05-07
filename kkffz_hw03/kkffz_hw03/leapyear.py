try:
    year = int(input("Enter a year: "))
except ValueError:
    print("Invalid input.")
    print("Program quits.")
else:
    if year <= 0:
        print("Invalid input.")
        print("Program quits.")
    else:
        is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
        if is_leap:
            print(f"Yes, {year} is a leap year.")
        else:
            print(f"No, {year} is not a leap year.")
