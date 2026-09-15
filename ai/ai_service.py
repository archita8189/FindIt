from ai.matcher import find_matches
from ai.entity_extractor import extract_entities
from ai.confidence import calculate_confidence


def process_lost_item(lost_description, found_items):
    """
    Main AI Service

    Input:
        lost_description -> string
        found_items -> list of dictionaries from database

    Output:
        List of matched items with confidence and extracted entities
    """

    # Step 1: Find semantic matches
    matches = find_matches(
        lost_description,
        found_items
    )

    # Step 2: Extract entities from lost item
    lost_entities = extract_entities(
        lost_description
    )

    final_results = []

    # Step 3: Improve every match
    for _, row in matches.iterrows():

        found_entities = extract_entities(
            row["description"]
        )

        confidence = calculate_confidence(
            semantic_score=row["confidence"],
            lost_entities=lost_entities,
            found_entities=found_entities
        )

        final_results.append({

            "id": row["id"],

            "description": row["description"],

            "semantic_score": round(
                row["confidence"], 2
            ),

            "entities": found_entities,

            "confidence": confidence["confidence"],

            "status": confidence["status"]

        })

    return final_results