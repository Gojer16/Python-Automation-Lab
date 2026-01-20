#!/usr/bin/env python3
"""
Robust Financial Data Formatter (Pure Python)
Updated to include error handling, input validation, and multiple data sources.
"""

import sys
import json
import csv
import argparse
from typing import List, Tuple, Optional

def validate_financial_data(revenue: any, profit: any) -> Optional[Tuple[float, float]]:
    """Validates and converts revenue/profit data to floats."""
    try:
        rev = float(revenue)
        prof = float(profit)
        
        if rev == 0:
            print(f"⚠️  Warning: Skipping row with zero revenue (profit: {prof})", file=sys.stderr)
            return None
            
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
            next(reader, None) # Skip potential header
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

def format_and_print_table(data: List[Tuple[float, float]]) -> None:
    """Formats and prints financial data as a table using f-strings."""
    if not data:
        print("⚠️  No valid data to display.")
        return
    
    print('REVENUE | PROFIT | PERCENT')
    print('-' * 28)
    
    for revenue, profit in data:
        try:
            percent = profit / revenue
            print(f'{revenue:>7,.2f} | {profit:>+7.2f} | {percent:>7.2%}')
        except ZeroDivisionError:
             print(f'{revenue:>7,.2f} | {profit:>+7.2f} | {"N/A":>7}')

def main():
    parser = argparse.ArgumentParser(description="Robust Financial Data Formatter")
    parser.add_argument('file', nargs='?', help='Input file (CSV or JSON)')
    args = parser.parse_args()

    if args.file:
        if args.file.endswith('.csv'):
            data = load_data_from_csv(args.file)
        elif args.file.endswith('.json'):
            data = load_data_from_json(args.file)
        else:
            print("❌ Input file must be .csv or .json")
            return
    else:
        # Default to hardcoded data if no file provided
        data = load_data_from_hardcoded()

    format_and_print_table(data)

if __name__ == "__main__":
    main()