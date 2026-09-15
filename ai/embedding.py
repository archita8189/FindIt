from sentence_transformers import SentenceTransformer

# Load model only once
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_model():
    return model