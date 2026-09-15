import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Known colors
COLORS = {
    "black", "white", "blue", "red", "grey",
    "gray", "brown", "green", "purple", "silver"
}

# Known item types
ITEMS = {
    "backpack", "bag", "wallet", "phone", "laptop",
    "charger", "earbuds", "watch", "umbrella",
    "bottle", "headphones", "calculator",
    "purse", "speaker", "ipad", "keys",
    "keychain", "tablet"
}

# Known brands
BRANDS = {
    "apple", "nike", "adidas", "wildcraft",
    "hp", "dell", "lenovo", "boat",
    "jbl", "samsung", "realme",
    "oneplus", "mi", "skybag",
    "titan", "casio", "puma"
}


def extract_entities(description):

    text = description.lower()

    doc = nlp(text)

    entities = {
        "brand": None,
        "color": None,
        "item": None,
        "location": None
    }

    # Brand
    for brand in BRANDS:
        if brand in text:
            entities["brand"] = brand.title()

    # Color
    for color in COLORS:
        if color in text:
            entities["color"] = color.title()

    # Item
    for item in ITEMS:
        if item in text:
            entities["item"] = item.title()

    # Location
    for ent in doc.ents:
        if ent.label_ in ["GPE", "LOC", "FAC"]:
            entities["location"] = ent.text.title()

    return entities