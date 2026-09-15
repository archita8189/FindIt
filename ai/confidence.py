def calculate_confidence(
    semantic_score,
    lost_entities,
    found_entities
):
    """
    Calculates final confidence score by combining:
    - Semantic Similarity
    - Brand Match
    - Color Match
    - Item Match
    - Location Match

    Parameters:
        semantic_score (float): Semantic similarity (0-100)
        lost_entities (dict): Extracted entities from lost item
        found_entities (dict): Extracted entities from found item

    Returns:
        dict
    """

    final_score = semantic_score

    # ------------------------
    # Brand Matching
    # ------------------------
    if (
        lost_entities.get("brand")
        and found_entities.get("brand")
    ):
        if lost_entities["brand"].lower() == found_entities["brand"].lower():
            final_score += 10
        else:
            final_score -= 25

    # ------------------------
    # Color Matching
    # ------------------------
    if (
        lost_entities.get("color")
        and found_entities.get("color")
    ):
        if lost_entities["color"].lower() == found_entities["color"].lower():
            final_score += 5
        else:
            final_score -= 25

    # ------------------------
    # Item Matching
    # ------------------------
    if (
        lost_entities.get("item")
        and found_entities.get("item")
    ):
        if lost_entities["item"].lower() == found_entities["item"].lower():
            final_score += 5
        else:
            final_score -= 20

    # ------------------------
    # Location Matching
    # ------------------------
    if (
        lost_entities.get("location")
        and found_entities.get("location")
    ):
        if lost_entities["location"].lower() == found_entities["location"].lower():
            final_score += 3

    # Keep score between 0 and 100
    final_score = max(0, min(100, final_score))

    # Match Status
    if final_score >= 85:
        status = "Excellent Match"
    elif final_score >= 70:
        status = "Strong Match"
    elif final_score >= 50:
        status = "Possible Match"
    else:
        status = "No Reliable Match"

    return {
        "confidence": round(final_score, 2),
        "status": status
    }