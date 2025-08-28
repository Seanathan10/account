CATEGORY_TAGS = [
    "Rent",
    "Mortgage payments",
    "Home insurance",
    "Property taxes",
    "Maintenance and repairs",
    "Electricity",
    "Water",
    "Gas",
    "Internet",
    "Cable",
    "Fuel",
    "Public transit costs",
    "Vehicle maintenance",
    "Parking fees",
    "Car payments",
    "Food",
    "Groceries",
    "Dining out",
    "Fast food",
    "Health insurance premiums",
    "Doctor visits",
    "Prescriptions",
    "Dental care",
    "Movies",
    "Concerts",
    "Sporting events",
    "Books",
    "Hobbies",
    "Savings account deposits",
    "Retirement contributions",
    "Investment purchases",
    "Tuition",
    "School supplies",
    "Student loans",
    "Online courses",
    "Product sales",
    "Service fees",
    "Royalties",
    "Investment income",
    "Raw materials",
    "Direct labor",
    "Manufacturing supplies",
    "Shipping costs",
    "Salaries and wages",
    "Rent or lease payments",
    "Utility expenses",
    "Marketing and advertising",
    "Professional services (e.g., legal, consulting)",
    "Equipment purchases",
    "Building improvements",
    "Technology upgrades",
    "Income tax",
    "Sales tax",
    "Payroll tax",
    "Property tax",
    "Interest payments",
    "Principal repayments",
    "Travel and entertainment",
    "Insurance premiums",
    "Office supplies",
]

RULES = {}

RULES.update({k: "Dining out" for k in [
    "coffee",
    "starbucks",
    "dunkin",
    "peets",
    "tim hortons",
    "caribou coffee",
    "coffee bean",
    "blue bottle",
    "philz",
    "cafe",
    "restaurant",
    "bistro",
    "eatery",
    "brunch",
    "diner",
    "steakhouse",
    "olive garden",
    "chilis",
    "applebee",
    "outback",
    "panera",
]})

RULES.update({k: "Groceries" for k in [
    "grocery",
    "safeway",
    "walmart",
    "target",
    "costco",
    "whole foods",
    "trader joe",
    "aldi",
    "kroger",
    "publix",
    "giant",
    "meijer",
    "heb",
    "food lion",
    "winco",
    "piggly wiggly",
    "shoprite",
    "wegmans",
    "stop & shop",
    "sprouts",
]})

RULES.update({k: "Fuel" for k in [
    "chevron",
    "shell",
    "exxon",
    "bp",
    "76",
    "valero",
    "mobil",
    "texaco",
    "arco",
    "speedway",
    "sunoco",
    "marathon",
    "gulf",
    "circle k",
    "phillips 66",
]})

RULES.update({k: "Public transit costs" for k in [
    "uber",
    "lyft",
    "metro",
    "subway ride",
    "bus",
    "train",
    "tram",
    "ride share",
    "taxi",
    "bart",
]})

RULES.update({k: "Insurance premiums" for k in [
    "aaa",
    "geico",
    "state farm",
    "progressive",
    "allstate",
    "farmers insurance",
    "nationwide",
    "liberty mutual",
    "usaa",
    "metlife",
]})

RULES.update({k: "Fast food" for k in [
    "mcdonald",
    "burger king",
    "kfc",
    "subway",
    "domino",
    "pizza hut",
    "chipotle",
    "taco bell",
    "wendy",
    "panera bread",
    "dunkin donuts",
    "panda express",
    "shake shack",
    "five guys",
    "little caesars",
    "sonic",
    "arbys",
    "jack in the box",
    "qdoba",
    "whataburger",
]})

RULES.update({k: "Books" for k in [
    "barnes & noble",
    "bookstore",
    "books-a-million",
    "powell's",
    "bookshop",
]})

RULES.update({k: "Hobbies" for k in [
    "gamestop",
    "michaels",
    "joann",
    "hobby lobby",
    "guitar center",
]})

RULES.update({k: "Travel and entertainment" for k in [
    "delta",
    "united",
    "american airlines",
    "southwest",
    "jetblue",
    "marriott",
    "hilton",
    "airbnb",
    "lyric",
    "amtrak",
]})

RULES.update({k: "Office supplies" for k in [
    "staples",
    "office depot",
    "office max",
    "paper source",
    "quill",
]})

RULES.update({k: "Online courses" for k in [
    "udemy",
    "coursera",
    "edx",
    "pluralsight",
    "skillshare",
]})

RULES.update({k: "Tuition" for k in [
    "university",
    "college",
    "tuition",
    "bursar",
    "campus payment",
]})

RULES.update({k: "Student loans" for k in [
    "nelnet",
    "navient",
    "fedloan",
    "great lakes",
    "mohela",
]})

RULES.update({k: "Doctor visits" for k in [
    "clinic",
    "hospital",
    "medical center",
    "doctor",
    "urgent care",
]})

RULES.update({k: "Prescriptions" for k in [
    "pharmacy",
    "cvs",
    "walgreens",
    "rite aid",
    "medication",
]})

RULES.update({k: "Dental care" for k in [
    "dentist",
    "orthodontist",
    "dental clinic",
    "periodontist",
    "endodontist",
]})

RULES.update({k: "Electricity" for k in [
    "electric bill",
    "pge",
    "duke energy",
    "coned",
    "southern company",
]})

RULES.update({k: "Water" for k in [
    "water bill",
    "aquafina",
    "american water",
    "suez water",
    "veolia water",
]})

RULES.update({k: "Gas" for k in [
    "gas bill",
    "so cal gas",
    "national grid gas",
    "centerpoint energy",
    "peoples gas",
]})

RULES.update({k: "Internet" for k in [
    "comcast",
    "xfinity",
    "spectrum",
    "cox",
    "verizon fios",
]})

RULES.update({k: "Cable" for k in [
    "directv",
    "dish",
    "xfinity cable",
    "sling tv",
    "charter cable",
]})

RULES.update({k: "Vehicle maintenance" for k in [
    "jiffy lube",
    "firestone",
    "pep boys",
    "maaco",
    "midas",
]})

RULES.update({k: "Parking fees" for k in [
    "parking",
    "meter",
    "garage",
    "parkmobile",
    "paybyphone",
]})

RULES.update({k: "Car payments" for k in [
    "ford credit",
    "toyota financial",
    "honda finance",
    "ally auto",
    "nissan motor",
]})


def categorize(description: str) -> str:
    desc = description.lower()
    for keyword, category in RULES.items():
        if keyword in desc:
            return category
    return "Uncategorized"
