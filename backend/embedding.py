from sentence_transformers import SentenceTransformer

# Load AI embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

text = """
ABC Pvt Ltd entered into a commercial contract with XYZ Ltd.
The defendant failed to make payment within the agreed period.
The plaintiff sought damages for breach of contract.
"""

embedding = model.encode(text)

print("Embedding generated successfully!")
print("Vector length:", len(embedding))