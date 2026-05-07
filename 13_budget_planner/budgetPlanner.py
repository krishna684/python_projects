"""Budget planner for the final project."""


def normalize_month_name(month_name: str) -> str:
    """Normalize a month name to the short form used by the data files."""
    return month_name.strip().lower()


def load_month_expenses(month_name: str) -> dict[str, float]:
    """Load category totals for one month from its expense file."""
    file_name = f"{month_name}_expenses.txt"
    category_totals: dict[str, float] = {}

    try:
        source = open(file_name, "r", encoding="utf-8")
    except FileNotFoundError:
        print(f"You do not have the expenses record for {month_name}.")
        return category_totals

    with source:
        for raw_line in source:
            text = raw_line.strip()
            if not text:
                continue

            parts = text.split(",")
            if len(parts) < 3:
                continue

            amount_text = parts[1].strip()
            category = parts[2].strip().lower()

            if not category:
                continue

            try:
                amount = float(amount_text)
            except ValueError:
                continue

            category_totals[category] = category_totals.get(category, 0.0) + amount

    return category_totals


def collect_selected_months(raw_months: str) -> list[str]:
    """Split the user input into valid month names in the given order."""
    valid_months = ["jan", "feb", "mar", "apr", "may"]
    selected_months: list[str] = []
    seen_months: dict[str, bool] = {}

    for part in raw_months.split(","):
        month = normalize_month_name(part)

        if not month:
            continue

        if month in valid_months:
            if month not in seen_months:
                selected_months.append(month)
                seen_months[month] = True
            continue

        if month:
            print(f"You do not have the expenses record for {month}.")

    return selected_months


def build_budget(selected_months: list[str]) -> tuple[dict[str, float], float, list[str]]:
    """Calculate regular budgets, sinking fund total, and sinking categories."""
    month_count = len(selected_months)
    category_totals: dict[str, float] = {}
    category_month_counts: dict[str, int] = {}

    for month in selected_months:
        month_expenses = load_month_expenses(month)
        seen_in_month: dict[str, bool] = {}

        for category, amount in month_expenses.items():
            category_totals[category] = category_totals.get(category, 0.0) + amount
            if category not in seen_in_month:
                category_month_counts[category] = category_month_counts.get(category, 0) + 1
                seen_in_month[category] = True

    regular_budget: dict[str, float] = {}
    sinking_categories: list[str] = []
    sinking_total = 0.0

    for category, total_amount in category_totals.items():
        if category_month_counts.get(category, 0) > 1:
            regular_budget[category] = total_amount / month_count
        else:
            sinking_categories.append(category)
            sinking_total += total_amount

    sinking_budget = sinking_total / month_count if month_count else 0.0
    return regular_budget, sinking_budget, sinking_categories


def print_budget(regular_budget: dict[str, float], sinking_budget: float, sinking_categories: list[str]) -> None:
    """Print the final monthly budget in the expected format."""
    for category, amount in regular_budget.items():
        print(f"{category}: ${amount}")

    print()
    print(
        "Finally, you should leave "
        f"${sinking_budget} as sinking fund for occasional spending, such as things in the categories of:"
    )

    for category in sinking_categories:
        print(f"    {category}")


def main() -> None:
    """Run the budget planner."""
    raw_months = input("Which months' expenses should be used to plan the budget: ").strip()
    selected_months = collect_selected_months(raw_months)

    if len(selected_months) < 2:
        print("Insufficient data to calculate the budget. You select more than one month.")
        return

    regular_budget, sinking_budget, sinking_categories = build_budget(selected_months)

    print("Based on the analysis of your expenses for the selected months, your budget is calculated as follows:")
    print_budget(regular_budget, sinking_budget, sinking_categories)


if __name__ == "__main__":
    main()