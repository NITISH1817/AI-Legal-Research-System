import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("legal_cases")

query = input("Enter legal query: ")

embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[embedding],
    n_results=3
)

for i in range(len(results["ids"][0])):
    print("=" * 50)
    print("Case:", results["ids"][0][i])
    print()
    print(results["documents"][0][i][:500])
    print("\n")