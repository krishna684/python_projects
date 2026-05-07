def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def main():
    while True:
        user_input = input("Enter a year: ")
        if user_input.strip().lower() == "done":
            print("Exit.")
            break
        try:
            year = int(user_input)
            if year <= 0:
                print("Invalid input. Please enter a positive integer.")
                continue
            if is_leap_year(year):
                print(f"Yes, {year} is a leap year.")
            else:
                print(f"No, {year} is not a leap year.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

if __name__ == "__main__":
    main()
