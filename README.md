# Minimal Accounting App

A simple Flask-based bookkeeping application allowing manual transaction entry and automatic categorization.
The interface uses Tailwind CSS and JavaScript for a fast, modern experience that updates without page reloads.

## Features

- Add income and expense transactions manually.
- Display transactions in a sortable table with invoice PDF links.
- Auto-categorize transactions based on simple keyword rules and selectable tags.
- Visualize running balance over time with a dynamic line chart.

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
