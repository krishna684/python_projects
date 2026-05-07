def parse_number_list(user_input):
    return [int(item.strip()) for item in user_input.split(",")]


while True:
    list1 = parse_number_list(input("Enter the first list of numbers (comma-separated): "))
    list2 = parse_number_list(input("Enter the second list of numbers (comma-separated): "))

    if len(list1) != len(list2):
        print("The two lists must have the same length. Please try again.\n")
        continue

    result = []
    for i in range(len(list1)):
        result.append(list1[i] + list2[i])

    print("Result:", result)
    break
