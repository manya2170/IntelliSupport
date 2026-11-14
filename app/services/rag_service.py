
import json
from pathlib import Path

import faiss
from sentence_transformers import SentenceTransformer

from app.services.ai_service import generate_ai_response


# Locate the knowledge base files
BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge_base"

DOCUMENTS_PATH = KNOWLEDGE_DIR / "documents.json"
INDEX_PATH = KNOWLEDGE_DIR / "support.index"


# Load knowledge base documents
with open(DOCUMENTS_PATH, "r", encoding="utf-8") as file:
    knowledge_base = json.load(file)


# Load embedding model and FAISS index
embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

index = faiss.read_index(str(INDEX_PATH))


def generate_rag_response(customer_message):

    # Convert customer question into an embedding
    query_embedding = embedding_model.encode(
        [customer_message],
        convert_to_numpy=True,
        normalize_embeddings=True
    ).astype("float32")

    # Find the two most relevant documents
    scores, indices = index.search(query_embedding, k=2)

    retrieved_context = []

    for idx, score in zip(indices[0], scores[0]):

        if idx != -1 and score >= 0.30:

            document = knowledge_base[idx]

            retrieved_context.append(
                f"Category: {document['category']}\n"
                f"Information: {document['content']}"
            )

    context = "\n\n".join(retrieved_context)

    if not context:
        context = "No relevant information was found in the knowledge base."

    # Generate an answer using Groq
    return generate_ai_response(
        customer_message,
        context=context
    )
