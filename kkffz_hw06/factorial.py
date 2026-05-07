# factorial.py
# This program asks the user for a positive integer and computes its factorial using a for loop.

while True:
    user_input = input("Enter a positive integer: ")
    if user_input.lower() == "done":
        break
    try:
        n = int(user_input)
        if n <= 0:
            print("Invalid input.")
            continue
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        print(f"{n}! = {factorial}")
    except ValueError:
        print("Invalid input.")
