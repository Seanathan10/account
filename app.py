from datetime import datetime
from flask import Flask, render_template, request, redirect, jsonify, send_file
from io import BytesIO, StringIO
import csv


from database import (
    init_db,
    add_transaction,
    get_transactions,
    get_transaction,
    delete_transaction,
)
from categorizer import categorize, CATEGORY_TAGS
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
)
from reportlab.lib.styles import getSampleStyleSheet

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
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = [Paragraph("Invoice", styles["Title"]), Spacer(1, 12)]
    data = [
        ["Field", "Value"],
        ["Transaction ID", tx[0]],
        ["Date", tx[1]],
        ["Description", tx[2]],
        ["Category", tx[4]],
        ["Amount", f"${abs(tx[3]):.2f}"],
    ]
    table = Table(data, colWidths=[150, 300])
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ]
        )
    )
    elements.append(table)
    elements.append(Spacer(1, 24))
    elements.append(Paragraph("Thank you for your business.", styles["Normal"]))
    doc.build(elements)
    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name="invoice.pdf",
        mimetype="application/pdf",
    )


@app.route("/import", methods=["POST"])
def import_csv():
    file = request.files.get("file")
    if not file:
        return redirect("/")
    stream = StringIO(file.stream.read().decode("utf-8"))
    reader = csv.DictReader(stream)
    for row in reader:
        date = row.get("date") or datetime.now().strftime("%Y-%m-%d")
        description = row.get("description", "")
        try:
            amount = float(row.get("amount", 0))
        except ValueError:
            continue
        tx_type = row.get("type", "expense").lower()
        amount = abs(amount) if tx_type == "income" else -abs(amount)
        category = row.get("category") or categorize(description)
        add_transaction(date, description, amount, category)
    return redirect("/")


@app.route("/delete/<int:tx_id>", methods=["DELETE"]) 
def delete(tx_id: int):
    delete_transaction(tx_id)
    return ("", 204)



if __name__ == "__main__":
    app.run(debug=True)
