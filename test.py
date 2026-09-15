import pandas as pd
from ai.ai_service import process_lost_item

print("=" * 60)
print("        AI LOST & FOUND MATCHING SYSTEM")
print("=" * 60)

# Load temporary CSV
df = pd.read_csv("data/found_items.csv")

# User input
lost_item = input("\nDescribe your lost item:\n> ")

# Full AI Pipeline
results = process_lost_item(
    lost_item,
    df.to_dict(orient="records")
)

print("\n🔍 FINAL AI RESULTS\n")

for i, item in enumerate(results, start=1):

    print("=" * 50)
    print(f"🏆 Match #{i}")
    print("=" * 50)

    print(f"🆔 Item ID      : {item['id']}")
    print(f"📝 Description  : {item['description']}")
    print(f"🧠 Semantic     : {item['semantic_score']:.2f}%")
    print(f"🎯 Confidence   : {item['confidence']:.2f}%")
    print(f"📌 Status       : {item['status']}")

    print("\n📋 Entities")
    print("-" * 25)

    print("Brand    :", item["entities"]["brand"])
    print("Color    :", item["entities"]["color"])
    print("Item     :", item["entities"]["item"])
    print("Location :", item["entities"]["location"])
    print()