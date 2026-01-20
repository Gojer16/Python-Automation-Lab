"""
Robust Financial Data Formatter (Using Tabulate)
Updated to include error handling, input validation, and multiple data sources.
"""

import sys
import json
import csv
import argparse
from typing import List, Tuple, Optional

try:
    from tabulate import tabulate
except ImportError:
    print("❌ Error: 'tabulate' library not found. Install it with: pip install tabulate")
    sys.exit(1)

def validate_financial_data(revenue: any, profit: any) -> Optional[Tuple[float, float]]:
    """Validates and converts revenue/profit data to floats."""
    try:
        rev = float(revenue)
        prof = float(profit)
        return (rev, prof)
    except (ValueError, TypeError) as e:
        print(f"❌ Error: Invalid data - revenue: {revenue}, profit: {profit} ({e})", file=sys.stderr)
        return None

def load_data_from_hardcoded() -> List[Tuple[float, float]]:
    """Returns the original hardcoded dataset."""
    return [
        (1000, 10),
        (2000, 17),
        (2500, 170),
        (2500, -170),
    ]

def load_data_from_csv(filepath: str) -> List[Tuple[float, float]]:
    """Loads financial data from a CSV file."""
    data = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader, None) # Skip header
            for row in reader:
                if len(row) >= 2:
                    validated = validate_financial_data(row[0], row[1])
                    if validated: data.append(validated)
        return data
    except Exception as e:
        print(f"❌ Error reading CSV: {e}", file=sys.stderr)
        return []

def load_data_from_json(filepath: str) -> List[Tuple[float, float]]:
    """Loads financial data from a JSON file."""
    data = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
            
        items = json_data if isinstance(json_data, list) else []
        for item in items:
            if isinstance(item, dict):
                validated = validate_financial_data(item.get('revenue'), item.get('profit'))
                if validated: data.append(validated)
            elif isinstance(item, (list, tuple)) and len(item) >= 2:
                validated = validate_financial_data(item[0], item[1])
                if validated: data.append(validated)
        return data
    except Exception as e:
        print(f"❌ Error reading JSON: {e}", file=sys.stderr)
        return []

def main():
    parser = argparse.ArgumentParser(description="Robust Financial Data Formatter (Tabulate)")
    parser.add_argument('file', nargs='?', help='Input file (CSV or JSON)')
    parser.add_argument('--format', default='simple', help='Table format (simple, grid, fancy_grid)')
    args = parser.parse_args()

    # Load Data
    if args.file:
        if args.file.endswith('.csv'):
            data = load_data_from_csv(args.file)
        elif args.file.endswith('.json'):
            data = load_data_from_json(args.file)
        else:
            print("❌ Input file must be .csv or .json")
            return
    else:
        data = load_data_from_hardcoded()

    # Process Data
    processed_data = []
    for revenue, profit in data:
        if revenue == 0:
             processed_data.append([revenue, profit, "N/A"])
        else:
             percent = profit / revenue
             processed_data.append([revenue, profit, percent])

    if not processed_data:
        print("⚠️  No valid data to display.")
        return

    # Print with Tabulate
    print(tabulate(
        processed_data, 
        headers=['REVENUE', 'PROFIT', 'PERCENT'], 
        tablefmt=args.format, 
        floatfmt=(",.2f", "+.2f", ".2%")
    ))

if __name__ == "__main__":
    main()