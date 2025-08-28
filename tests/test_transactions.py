import os
import sys
import pathlib

# Add project root to sys.path for imports
sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from database import init_db, add_transaction, get_transactions, DB_PATH
from categorizer import categorize
from app import app as flask_app
import io



def setup_module(module):
    if DB_PATH.exists():
        DB_PATH.unlink()
    init_db()


def teardown_module(module):
    if DB_PATH.exists():
        DB_PATH.unlink()


def test_add_and_list():
    add_transaction('2023-01-01', 'Coffee shop', -3.50, categorize('Coffee shop'))
    add_transaction('2023-01-02', 'Uber ride', -12.00, categorize('Uber ride'))
    txs = get_transactions()
    assert len(txs) == 2
    assert txs[0][2] == 'Uber ride'
    assert txs[0][4] == 'Public transit costs'


def test_categorize():
    assert categorize('Morning coffee') == 'Dining out'
    assert categorize('Unknown purchase') == 'Uncategorized'
    assert categorize('Chevron Gas') == 'Fuel'
    assert categorize('Safeway Store') == 'Groceries'
    assert categorize('AAA Insurance') == 'Insurance premiums'



def test_add_via_json_and_invoice():
    client = flask_app.test_client()
    resp = client.post('/add', json={'description': 'Book', 'amount': 10.0, 'type': 'expense'})
    assert resp.status_code == 200
    data = resp.get_json()
    assert data['description'] == 'Book'
    assert data['amount'] == -10.0
    assert data['category'] == 'Uncategorized'
    assert any(t[0] == data['id'] for t in get_transactions())

    resp2 = client.post('/add', json={'description': 'Salary', 'amount': 100.0, 'type': 'income'})
    assert resp2.get_json()['amount'] == 100.0

    inv = client.get(f"/invoice/{data['id']}")
    assert inv.status_code == 200
    assert inv.headers['Content-Type'] == 'application/pdf'


def test_delete_transaction():
    client = flask_app.test_client()
    resp = client.post('/add', json={'description': 'Temp item', 'amount': 5.0, 'type': 'expense'})
    tx_id = resp.get_json()['id']
    del_resp = client.delete(f'/delete/{tx_id}')
    assert del_resp.status_code == 204
    assert all(t[0] != tx_id for t in get_transactions())


def test_import_csv():
    client = flask_app.test_client()
    csv_data = 'date,description,amount,type,category\n2023-03-01,Imported Item,8,expense,Dining out\n'
    data = {
        'file': (io.BytesIO(csv_data.encode()), 'import.csv')
    }
    resp = client.post('/import', data=data, content_type='multipart/form-data')
    assert resp.status_code == 302
    assert any(t[2] == 'Imported Item' for t in get_transactions())

