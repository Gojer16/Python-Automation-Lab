# 🚀 Robust Financial Formatter - Usage Guide

## Overview

I've created **production-ready** versions of both scripts that fix all 5 issues you identified:

1. ✅ **Division by zero protection** - Validates and skips zero revenue entries
2. ✅ **Input validation** - Type checking and error handling for all data
3. ✅ **Multiple data sources** - CSV, JSON, interactive input, or hardcoded
4. ✅ **Comprehensive error handling** - Try-catch blocks with helpful error messages
5. ✅ **Font-agnostic output** - Uses proper alignment and formatting

---

## Files Created

| File | Description |
|------|-------------|
| `recipe_format_strings_robust.py` | Pure Python version (no dependencies) |
| `recipe_library_robust.py` | Tabulate library version (cleaner output) |
| `sample_data.csv` | Sample CSV file for testing |
| `sample_data.json` | Sample JSON file for testing |

---

## Installation

### For Format Strings Version (No dependencies)
```bash
# Ready to use immediately!
python recipe_format_strings_robust.py
```

### For Tabulate Version (Requires library)
```bash
# Install tabulate first
pip install tabulate

# Then run
python recipe_library_robust.py
```

---

## Usage Examples

### 1️⃣ **Using Hardcoded Data** (Default)

```bash
python recipe_format_strings_robust.py
```

Output:
```
🚀 Robust Financial Data Formatter

ℹ️  Using hardcoded sample data (use --help for other options)

=============================================
     REVENUE |       PROFIT |      PERCENT
=============================================
    1,000.00 |       +10.00 |        1.00%
    2,000.00 |       +17.00 |        0.85%
    2,500.00 |      +170.00 |        6.80%
    2,500.00 |      -170.00 |       -6.80%
=============================================
Total rows: 4
```

---

### 2️⃣ **Loading from CSV File**

```bash
python recipe_format_strings_robust.py sample_data.csv
```

Features:
- Auto-detects and skips header rows
- Validates each row
- Shows warnings for invalid data
- Skips rows with zero revenue

---

### 3️⃣ **Loading from JSON File**

```bash
python recipe_library_robust.py sample_data.json
```

Supports two JSON formats:

**Format 1: Array of objects**
```json
[
  {"revenue": 1000, "profit": 10},
  {"revenue": 2000, "profit": 17}
]
```

**Format 2: Array of arrays**
```json
[
  [1000, 10],
  [2000, 17]
]
```

---

### 4️⃣ **Interactive Input Mode**

```bash
python recipe_format_strings_robust.py --input
```

Interactive session:
```
📊 Enter financial data (type 'done' when finished)
Format: revenue profit (e.g., '1000 10')

Enter revenue and profit (or 'done'): 1000 10
✅ Added: Revenue=1,000.00, Profit=+10.00
Enter revenue and profit (or 'done'): 2000 17
✅ Added: Revenue=2,000.00, Profit=+17.00
Enter revenue and profit (or 'done'): done

✅ Collected 2 valid records
```

---

### 5️⃣ **Custom Table Formats** (Tabulate version only)

```bash
# Simple format (default)
python recipe_library_robust.py --format simple sample_data.csv

# Grid format (with borders)
python recipe_library_robust.py --format grid sample_data.csv

# GitHub markdown format
python recipe_library_robust.py --format github sample_data.csv

# Fancy grid (beautiful!)
python recipe_library_robust.py --format fancy_grid sample_data.csv
```

Available formats: `simple`, `grid`, `github`, `fancy_grid`, `pipe`, `orgtbl`, `rst`, `mediawiki`, `html`, `latex`

---

## Error Handling Examples

### ❌ Zero Revenue Detection

**Input CSV:**
```csv
revenue,profit
1000,10
0,50
2000,17
```

**Output:**
```
⚠️  Warning: Skipping row with zero revenue (profit: 50.0)
✅ Loaded 2 valid records from CSV
```

---

### ❌ Invalid Data Types

**Input CSV:**
```csv
revenue,profit
1000,10
abc,xyz
2000,17
```

**Output:**
```
❌ Error: Invalid data - revenue: abc, profit: xyz (could not convert string to float: 'abc')
✅ Loaded 2 valid records from CSV
```

---

### ❌ Missing File

```bash
python recipe_format_strings_robust.py nonexistent.csv
```

**Output:**
```
❌ Error: File not found: nonexistent.csv
⚠️  No data to display!
```

---

## Advanced Features

### 📊 Summary Statistics (Tabulate version)

The tabulate version includes automatic summary calculations:

```
📈 Summary:
   Total Revenue: $23,500.00
   Total Profit:  $+727.00
   Avg Margin:    3.09%
```

---

### 🎨 Emoji Indicators

Both scripts use emojis for better UX:
- ✅ Success messages
- ⚠️  Warnings (non-fatal issues)
- ❌ Errors (fatal issues)
- ℹ️  Information
- 📊 Data-related messages
- 🚀 Launch/startup

---

## Creating Your Own Data Files

### CSV Format

```csv
revenue,profit
1000,10
2000,17
```

- First row can be headers (auto-detected)
- Two columns: revenue, profit
- Numbers can have decimals

### JSON Format

**Option 1: Objects**
```json
[
  {"revenue": 1000, "profit": 10},
  {"revenue": 2000, "profit": 17}
]
```

**Option 2: Arrays**
```json
[
  [1000, 10],
  [2000, 17]
]
```

---

## Web Data Integration (Future Enhancement)

To load data from web APIs, you can extend the scripts:

```python
import requests

def load_data_from_api(url: str) -> List[Tuple[float, float]]:
    """Loads financial data from a REST API."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        
        # Process JSON data (same as load_data_from_json)
        data = []
        for item in json_data:
            if isinstance(item, dict):
                validated = validate_financial_data(
                    item.get('revenue'), 
                    item.get('profit')
                )
                if validated:
                    data.append(validated)
        
        return data
    except Exception as e:
        print(f"❌ Error fetching from API: {e}")
        return []
```

Usage:
```bash
python recipe_format_strings_robust.py https://api.example.com/financial-data
```

---

## Comparison: Original vs Robust

| Feature | Original | Robust |
|---------|----------|--------|
| Division by zero | ❌ Crashes | ✅ Validates & skips |
| Invalid data | ❌ Crashes | ✅ Shows error, continues |
| Data sources | ❌ Hardcoded only | ✅ CSV, JSON, input, hardcoded |
| Error messages | ❌ Python traceback | ✅ User-friendly messages |
| Input validation | ❌ None | ✅ Type checking |
| Negative revenue | ❌ Silent | ✅ Warning shown |
| Empty data | ❌ Crashes | ✅ Graceful message |
| Help system | ❌ None | ✅ --help flag |
| Summary stats | ❌ None | ✅ Totals & averages (tabulate) |

---

## Testing the Scripts

### Quick Test
```bash
# Test with sample CSV
python recipe_format_strings_robust.py sample_data.csv

# Test with sample JSON
python recipe_library_robust.py sample_data.json

# Test interactive mode
python recipe_format_strings_robust.py --input
```

### Test Error Handling

Create a file `bad_data.csv`:
```csv
revenue,profit
1000,10
0,50
abc,xyz
2000,
,100
```

Run:
```bash
python recipe_format_strings_robust.py bad_data.csv
```

You'll see proper error handling for each invalid row!

---

## Command Reference

### Format Strings Version
```bash
python recipe_format_strings_robust.py                 # Hardcoded data
python recipe_format_strings_robust.py data.csv        # Load CSV
python recipe_format_strings_robust.py data.json       # Load JSON
python recipe_format_strings_robust.py --input         # Interactive
python recipe_format_strings_robust.py --help          # Show help
```

### Tabulate Version
```bash
python recipe_library_robust.py                        # Hardcoded data
python recipe_library_robust.py data.csv               # Load CSV
python recipe_library_robust.py data.json              # Load JSON
python recipe_library_robust.py --input                # Interactive
python recipe_library_robust.py --format grid data.csv # Custom format
python recipe_library_robust.py --help                 # Show help
```

---

## Next Steps

1. **Try the scripts** with the sample data files
2. **Create your own** CSV or JSON files
3. **Test error handling** with intentionally bad data
4. **Experiment with formats** (tabulate version)
5. **Extend functionality** (add web API support, database connections, etc.)

---

## Key Improvements Summary

✅ **Robust error handling** - Never crashes, always shows helpful messages  
✅ **Input validation** - Checks data types and values before processing  
✅ **Multiple data sources** - Flexible input options  
✅ **User-friendly output** - Clear messages with emoji indicators  
✅ **Production-ready** - Can be used in real automation workflows  
✅ **Well-documented** - Docstrings and comments throughout  
✅ **Type hints** - Better code clarity and IDE support  
✅ **Extensible** - Easy to add new features (web APIs, databases, etc.)

Enjoy your robust automation scripts! 🎉
