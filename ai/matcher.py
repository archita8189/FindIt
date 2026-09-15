import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from ai.embedding import get_model

# Load the AI model only once
model = get_model()


def find_matches(lost_description, found_items, top_k=3):
    """
    Finds the best matching found items using semantic similarity.

    Parameters:
        lost_description (str): Description of the lost item.
        found_items (list): List of dictionaries containing found item data.
        top_k (int): Number of top matches to return.

    Returns:
        pandas.DataFrame: Top matching items sorted by confidence.
    """

    # Convert list of dictionaries into DataFrame
    df = pd.DataFrame(found_items)

    # Safety check
    if df.empty:
        return df

    if "description" not in df.columns:
        raise ValueError("Each found item must contain a 'description' field.")

    # Generate embeddings
    found_embeddings = model.encode(df["description"].tolist())
    lost_embedding = model.encode([lost_description])

    # Calculate cosine similarity
    similarities = cosine_similarity(
        lost_embedding,
        found_embeddings
    )[0]

    # Convert similarity into percentage
    df["confidence"] = (similarities * 100).round(2)

    # Assign match status
      # Assign match status
    def get_status(score):
        if score >= 90:
            return "Excellent Match"
        elif score >= 80:
            return "High Match"
        elif score >= 70:
            return "Possible Match"
        elif score >= 40:
            return "Low Match"
        else:
            return "No Reliable Match"

    df["status"] = df["confidence"].apply(get_status)
    # Sort by confidence
    results = df.sort_values(
        by="confidence",
        ascending=False
    )

    # Return top matches
    return results.head(top_k).reset_index(drop=True)