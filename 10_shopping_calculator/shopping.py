def parse_price_line(line: str) -> tuple[str, str] | tuple[None, str]:
    """Validate and parse one line from prices.txt."""
    parts = line.strip().split(",")

    if len(parts) != 2:
        return None, "Wrong format."

    item = parts[0].strip()
    price_text = parts[1].strip()

    if not item or not price_text:
        return None, "Wrong format."

    try:
        float(price_text)
    except ValueError:
        return None, "The price must be a number."

    return f"{item},{price_text}", ""


def clean_prices_file(input_path: str, output_path: str) -> None:
    """Read prices file, report skipped lines, and write cleaned data."""
    cleaned_lines: list[str] = []

    with open(input_path, "r", encoding="utf-8") as file_in:
        for item_number, raw_line in enumerate(file_in, start=1):
            parsed_line, error_message = parse_price_line(raw_line)

            if parsed_line is None:
                print(f"Item #{item_number} skipped - {error_message}")
            else:
                cleaned_lines.append(parsed_line)

    with open(output_path, "w", encoding="utf-8") as file_out:
        for cleaned_line in cleaned_lines:
            file_out.write(cleaned_line + "\n")


def main() -> None:
    clean_prices_file("prices.txt", "prices_cleaned.txt")


if __name__ == "__main__":
    main()
