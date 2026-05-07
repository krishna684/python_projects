# Email Domain Analyzer

Analyzes email domains from archive files and counts domain occurrences.

## Files
- `countEmailDomain.py` - Domain counting utility
- `archive-02-20-2019.txt` - Archive 1 with email addresses
- `archive-03-02-2024.txt` - Archive 2 with email addresses
- `archive-08-05-2030.txt` - Archive 3 with email addresses

## Description
This program:
- Reads email addresses from archive files
- Extracts domain information (part after @)
- Counts frequency of each domain
- Displays domain statistics

## How to Run
```bash
python countEmailDomain.py
```

## Requirements
- Archive files must contain one email per line
- Supports multiple archive files
- Aggregates results across all files

## Output
Displays count of emails per domain:
```
domain1.com: 5
domain2.com: 3
domain3.com: 2
```
