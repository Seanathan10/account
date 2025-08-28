import sqlite3
from pathlib import Path

DB_PATH = Path("transactions.db")


def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            description TEXT NOT NULL,
            amount REAL NOT NULL,
            category TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def add_transaction(date: str, description: str, amount: float, category: str) -> int:
    """Insert a transaction and return its database id."""

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO transactions (date, description, amount, category) VALUES (?, ?, ?, ?)",
        (date, description, amount, category),
    )
    conn.commit()
    row_id = cur.lastrowid
    conn.close()
    return row_id



def get_transaction(tx_id: int):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "SELECT id, date, description, amount, category FROM transactions WHERE id=?",
        (tx_id,),
    )
    row = cur.fetchone()
    conn.close()
    return row


def get_transactions():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "SELECT id, date, description, amount, category FROM transactions ORDER BY date DESC"
    )
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_transaction(tx_id: int) -> None:
    """Remove a transaction from the database."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("DELETE FROM transactions WHERE id=?", (tx_id,))
    conn.commit()
    conn.close()

