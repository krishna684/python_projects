from pathlib import Path


def extract_domain_from_line(line):
    """Return the domain from a valid "From " line, or None if unavailable."""
    if not line.startswith("From "):
        return None

    pieces = line.split()
    if len(pieces) < 2 or "@" not in pieces[1]:
        return None

    _, domain = pieces[1].split("@", 1)
    return domain.lower()


def count_emails_from_domain(filename, target_domain):
    """Count how many sender emails match target_domain in the archive file."""
    count = 0
    archive_path = Path(__file__).resolve().parent / filename

    with archive_path.open("r") as archive_file:
        for line in archive_file:
            domain = extract_domain_from_line(line)
            if domain == target_domain:
                count += 1

    return count


def main():
    filename = input("Enter the filename for the email archive: ").strip()
    domain_to_count = input("Enter the domain: ").strip().lower()

    match_count = count_emails_from_domain(filename, domain_to_count)

    print(f"There are {match_count} emails from {domain_to_count}.")


if __name__ == "__main__":
    main()
