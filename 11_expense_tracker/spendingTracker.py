"""Simple spending and income tracker.

Reads existing entries from expenses.txt, lets the user summarize or add entries,
and writes only newly added entries back to the same file when done.
"""

from __future__ import annotations

from pathlib import Path


DATA_FILE = Path("expenses.txt")


def build_ledger(entries: list[tuple[str, float, str]]) -> dict[str, float | dict[str, float]]:
    """Build a dictionary-based ledger from entry tuples."""
    ledger: dict[str, float | dict[str, float]] = {
        "income_total": 0.0,
        "expense_total": 0.0,
        "expenses_by_category": {},
    }

    for _, amount, category in entries:
        update_ledger(ledger, amount, category)

    return ledger


def update_ledger(ledger: dict[str, float | dict[str, float]], amount: float, category: str) -> None:
    """Update dictionary totals after adding one entry."""
    if category == "income":
        ledger["income_total"] = float(ledger["income_total"]) + amount
        return

    ledger["expense_total"] = float(ledger["expense_total"]) + amount
    expenses_by_category = ledger["expenses_by_category"]
    if not isinstance(expenses_by_category, dict):
        expenses_by_category = {}
        ledger["expenses_by_category"] = expenses_by_category

    expenses_by_category[category] = float(expenses_by_category.get(category, 0.0)) + amount


def parse_entry(raw_line: str) -> tuple[str, float, str] | None:
    """Parse one CSV-like entry line: specification,amount,category."""
    text = raw_line.strip()
    if not text:
        return None

    parts = text.split(",", 2)
    if len(parts) != 3:
        return None

    specification = parts[0].strip()
    amount_text = parts[1].strip()
    category = parts[2].strip().lower()

    if not specification or not category:
        return None

    try:
        amount = float(amount_text)
    except ValueError:
        return None

    if amount < 0:
        return None

    return specification, amount, category


def load_entries(file_path: Path) -> list[tuple[str, float, str]]:
    """Load valid entries from disk and skip invalid lines."""
    entries: list[tuple[str, float, str]] = []

    if not file_path.exists():
        return entries

    with file_path.open("r", encoding="utf-8") as source:
        for line in source:
            parsed = parse_entry(line)
            if parsed is not None:
                entries.append(parsed)

    return entries


def summarize(ledger: dict[str, float | dict[str, float]]) -> None:
    """Print total income, expenses by category, total expense, and remaining."""
    income_total = float(ledger["income_total"])
    expense_total = float(ledger["expense_total"])
    expenses_by_category = ledger["expenses_by_category"]

    print(f"Income: {income_total:.1f}")
    print("Expenses:")
    if isinstance(expenses_by_category, dict):
        for category, amount in expenses_by_category.items():
            print(f"    {category}: ${float(amount):.1f}")

    print(f"Total: {expense_total:.1f}")
    print(f"Remaining: {income_total - expense_total:.1f}")


def ask_for_entry() -> tuple[str, float, str] | None:
    """Prompt user for one new entry and validate format and values."""
    raw = input("New entry (in the form of details,amount,category): ").strip()

    parsed = parse_entry(raw)
    if parsed is None:
        print("Invalid entry. Use: details,amount,category with a non-negative amount.")
        return None

    return parsed


def append_new_entries(file_path: Path, entries: list[tuple[str, float, str]]) -> None:
    """Append only new entries to the data file."""
    if not entries:
        return

    needs_leading_newline = False
    if file_path.exists() and file_path.stat().st_size > 0:
        with file_path.open("rb") as source:
            source.seek(-1, 2)
            last_byte = source.read(1)
            needs_leading_newline = last_byte != b"\n"

    with file_path.open("a", encoding="utf-8") as target:
        if needs_leading_newline:
            target.write("\n")

        for specification, amount, category in entries:
            target.write(f"{specification},{amount:g},{category}\n")


def main() -> None:
    existing_entries = load_entries(DATA_FILE)
    ledger = build_ledger(existing_entries)
    added_entries: list[tuple[str, float, str]] = []

    while True:
        operation = input("Choose an operation (summarize, add, done):").strip().lower()

        if operation == "summarize":
            summarize(ledger)
            print("\n-------------------")
        elif operation == "add":
            new_entry = ask_for_entry()
            if new_entry is not None:
                added_entries.append(new_entry)
                _, amount, category = new_entry
                update_ledger(ledger, amount, category)
            print("-------------------")
        elif operation == "done":
            append_new_entries(DATA_FILE, added_entries)
            print("New records are saved to expenses.txt.")
            break
        else:
            print("Invalid operation. Please choose summarize, add, or done.")


if __name__ == "__main__":
    main()
