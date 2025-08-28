import os
import sys
import pathlib

# Add project root to sys.path for imports
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from database import init_db, add_transaction, get_transactions, DB_PATH
from categorizer import categorize
from app import app as flask_app



def setup_module(module):
    if DB_PATH.exists():
        DB_PATH.unlink()
    init_db()


def teardown_module(module):
    if DB_PATH.exists():
        DB_PATH.unlink()


def test_add_and_list():
    add_transaction('2023-01-01', 'Coffee shop', 3.50, categorize('Coffee shop'))
    add_transaction('2023-01-02', 'Uber ride', 12.00, categorize('Uber ride'))
    txs = get_transactions()
    assert len(txs) == 2
    assert txs[0][2] == 'Uber ride'
    assert txs[0][4] == 'Transport'


def test_categorize():
    assert categorize('Morning coffee') == 'Food'
    assert categorize('Unknown purchase') == 'Uncategorized'


def test_add_via_json():
    client = flask_app.test_client()
    resp = client.post('/add', json={'description': 'Book', 'amount': 10.0})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['description'] == 'Book'
    assert data['category'] == 'Uncategorized'
    assert any(t[0] == data['id'] for t in get_transactions())

