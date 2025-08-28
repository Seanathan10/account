from datetime import datetime
from flask import Flask, render_template, request, redirect, jsonify


from database import init_db, add_transaction, get_transactions
from categorizer import categorize

app = Flask(__name__)
init_db()


@app.route("/", methods=["GET"])
def index():
    transactions = get_transactions()
    return render_template("index.html", transactions=transactions)


@app.route("/add", methods=["POST"])
def add():
    data = request.get_json(silent=True)
    if data:
        date = data.get("date") or datetime.now().strftime("%Y-%m-%d")
        description = data["description"]
        amount = float(data["amount"])
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
    category = request.form.get("category") or categorize(description)
    add_transaction(date, description, amount, category)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
