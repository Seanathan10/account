RULES = {
    "coffee": "Food",
    "grocery": "Groceries",
    "uber": "Transport",
}


def categorize(description: str) -> str:
    desc = description.lower()
    for keyword, category in RULES.items():
        if keyword in desc:
            return category
    return "Uncategorized"
