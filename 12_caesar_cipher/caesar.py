ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def shift_message(message, key, mode):
    """Return a Caesar-shifted message in lowercase, copying non-letters unchanged."""
    shifted = ""
    offset = key % len(ALPHABET)

    for char in message.lower():
        if char in ALPHABET:
            index = ALPHABET.index(char)
            if mode == "e":
                new_index = (index + offset) % len(ALPHABET)
            else:
                new_index = (index - offset) % len(ALPHABET)
            shifted += ALPHABET[new_index]
        else:
            shifted += char

    return shifted


def get_mode():
    """Prompt until user enters e, d, or Done."""
    while True:
        mode = input("Encrypt (e) or decrypt (d): ").strip()
        if mode == "Done":
            return "Done"
        mode = mode.lower()
        if mode in ("e", "d"):
            return mode
        print("Invalid mode. Must enter e or d.")


def main():
    while True:
        mode = get_mode()
        if mode == "Done":
            break

        key = int(input("Key: ").strip())

        if mode == "e":
            message = input("Plaintext: ")
            result = shift_message(message, key, mode)
            print("Encrypted to:", result)
        else:
            message = input("Ciphertext: ")
            result = shift_message(message, key, mode)
            print("Decrypted to:", result)

        print()


main()
