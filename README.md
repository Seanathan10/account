# Minimal Accounting App

A simple Flask-based bookkeeping application allowing manual transaction entry and automatic categorization.
The interface uses Tailwind CSS and JavaScript for a fast, modern experience that updates without page reloads.

## Features

- Add income and expense transactions manually.
- Display transactions in a sortable table with invoice PDF links and deletion.
- Auto-categorize transactions based on simple keyword rules and selectable tags.
- Visualize running balance over time with a dynamic line chart.
- Sort columns in ascending or descending order with header arrows.
- Over 150 keyword rules map common merchants to categories.
- Generate professional-looking PDF invoices for each entry.
- Import transactions in bulk from CSV files.

## Setup

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

Run tests:

```
pytest
```

Transactions are stored in `transactions.db` SQLite database.

### Importing CSV

Upload a CSV file with columns `date,description,amount,type,category` to `/import` using the form on the homepage. An example file `sample_transactions.csv` is included with ten sample records.
