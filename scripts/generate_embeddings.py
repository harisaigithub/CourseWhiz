from sentence_transformers import SentenceTransformer
import json
import numpy as np
import os

# File paths
DATA_FILE = "data/courses.json"
INDEX_FILE = "models/courses_index.npy"  # Changed to a NumPy array for simplicity

def generate_embeddings():
    """
    Generate embeddings for course descriptions and save as a NumPy array.
    """
    # Check if data file exists
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"Data file not found: {DATA_FILE}")

    # Load data
    with open(DATA_FILE, "r") as f:
        courses = json.load(f)

    # Check if data is valid
    if not courses or not isinstance(courses, list):
        raise ValueError("Courses data is invalid or empty.")

    # Initialize model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Generate embeddings
    descriptions = [course.get("description", "") for course in courses]
    embeddings = model.encode(descriptions)

    # Save embeddings as a NumPy array
    os.makedirs(os.path.dirname(INDEX_FILE), exist_ok=True)
    np.save(INDEX_FILE, embeddings)
    print(f"Embeddings saved to {INDEX_FILE}")

    # Save course metadata for lookup
    METADATA_FILE = "models/courses_metadata.json"
    with open(METADATA_FILE, "w") as meta_file:
        json.dump(courses, meta_file)
    print(f"Metadata saved to {METADATA_FILE}")

if __name__ == "__main__":
    generate_embeddings()
