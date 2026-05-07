def split_and_validate_name(name_text):
    parts = name_text.strip().split()

    if len(parts) != 2:
        return None, "Invalid input: please enter your first name and last name separated by a space."

    first_name, last_name = parts

    if not first_name.isalpha() or not last_name.isalpha():
        return None, "Invalid input: please only enter alphabetical letters."

    return (first_name.lower(), last_name.lower()), None


def build_local_part(first_name, last_name):
    return f"{first_name[0]}{len(first_name)}{last_name[0]}{len(last_name)}"


def main():
    while True:
        entered_name = input("Enter your name: ")

        if entered_name.strip() == "Done":
            break

        valid_name, error_message = split_and_validate_name(entered_name)

        if error_message is not None:
            print(error_message)
            continue

        first_name, last_name = valid_name
        local_part = build_local_part(first_name, last_name)
        print(f"Your email is: {local_part}")


main()
