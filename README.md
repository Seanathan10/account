# Minimal Accounting App

A simple Flask-based bookkeeping application allowing manual transaction entry and automatic categorization.
The interface uses Tailwind CSS and JavaScript for a fast, modern experience that updates without page reloads.

## Features

- Add transactions manually.
- Display transactions in a modern web interface.

- Auto-categorize transactions based on simple keyword rules.

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
