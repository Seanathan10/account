from datetime import datetime
from flask import Flask, render_template, request, redirect, jsonify, send_file
from io import BytesIO

from database import (
    init_db,
    add_transaction,
    get_transactions,
    get_transaction,
    delete_transaction,
)

from categorizer import categorize, CATEGORY_TAGS
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
init_db()


@app.route("/", methods=["GET"])
def index():
    transactions = get_transactions()
    return render_template("index.html", transactions=transactions, categories=CATEGORY_TAGS)



@app.route("/add", methods=["POST"])
def add():
    data = request.get_json(silent=True)
    if data:
        date = data.get("date") or datetime.now().strftime("%Y-%m-%d")
        description = data["description"]
        amount = float(data["amount"])
        tx_type = data.get("type", "expense")
        amount = abs(amount) if tx_type == "income" else -abs(amount)

        category = data.get("category") or categorize(description)
        tx_id = add_transaction(date, description, amount, category)
        return jsonify(
            {
                "id": tx_id,
                "date": date,
                "description": description,
                "amount": amount,
                "category": category,
            }
        )
    date = request.form.get("date") or datetime.now().strftime("%Y-%m-%d")
    description = request.form["description"]
    amount = float(request.form["amount"])
    tx_type = request.form.get("type", "expense")
    amount = abs(amount) if tx_type == "income" else -abs(amount)

    category = request.form.get("category") or categorize(description)
    add_transaction(date, description, amount, category)
    return redirect("/")


@app.route("/invoice/<int:tx_id>")
def invoice(tx_id: int):
    tx = get_transaction(tx_id)
    if not tx:
        return ("Not found", 404)
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)
    p.drawString(72, 720, "Invoice")
    p.drawString(72, 700, f"Transaction ID: {tx[0]}")
    p.drawString(72, 680, f"Date: {tx[1]}")
    p.drawString(72, 660, f"Description: {tx[2]}")
    p.drawString(72, 640, f"Amount: {tx[3]:.2f}")
    p.drawString(72, 620, f"Category: {tx[4]}")
    p.showPage()
    p.save()
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="invoice.pdf", mimetype="application/pdf")


@app.route("/delete/<int:tx_id>", methods=["DELETE"]) 
def delete(tx_id: int):
    delete_transaction(tx_id)
    return ("", 204)



if __name__ == "__main__":
    app.run(debug=True)
