# odd_total.py
# This program asks the user for a sequence of numbers separated by commas and calculates the sum of the numbers at odd indices.

while True:
    user_input = input("Enter a sequence of numbers separated by comma: ")
    if user_input.lower() == "done":
        break
    numbers = user_input.split(",")
    total = 0
    for i in range(1, len(numbers), 2):
        total += float(numbers[i])
    print(f"Total of the numbers at the odd indices = {total}")
