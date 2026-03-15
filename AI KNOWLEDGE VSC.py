# app.py
from flask import Flask, render_template, request, jsonify
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os

app = Flask(__name__)

# ---------------------------
# Load AI model
# ---------------------------
print("Loading sentence-transformers model...")
model = SentenceTransformer('all-MiniLM-L6-v2')
print("Model loaded successfully!")

# ---------------------------
# Load knowledge base
# ---------------------------
knowledge_file = os.path.join("data", "knowledge.txt")
if not os.path.exists(knowledge_file):
    raise FileNotFoundError(f"Knowledge file not found at {knowledge_file}. Please create it with sample sentences.")

with open(knowledge_file, "r", encoding="utf-8") as f:
    knowledge = [line.strip() for line in f if line.strip()]

if len(knowledge) == 0:
    raise ValueError("Knowledge file is empty. Add some sentences for the AI to use.")

# Precompute embeddings for all knowledge sentences
print("Encoding knowledge sentences...")
knowledge_embeddings = model.encode(knowledge)
print("Knowledge embeddings ready!")

# ---------------------------
# Routes
# ---------------------------
@app.route("/")
def home():
    return render_template("index.html")  # Make sure index.html is in a folder named "templates"

@app.route("/ask", methods=["POST"])
def ask():
    try:
        data = request.get_json()
        if not data or "question" not in data:
            return jsonify({"answer": "No question provided!"})

        query = data["question"].strip()
        if query == "":
            return jsonify({"answer": "Please type a question!"})

        # Encode the question
        query_embedding = model.encode([query])

        # Compute cosine similarity with all knowledge embeddings
        scores = cosine_similarity(query_embedding, knowledge_embeddings)

        # Find the best matching sentence
        best_index = np.argmax(scores)
        answer = knowledge[best_index]

        return jsonify({"answer": answer})

    except Exception as e:
        print("Error in /ask:", e)
        return jsonify({"answer": "Error processing your question."})

# ---------------------------
# Run the Flask app
# ---------------------------
if __name__ == "__main__":
    # debug=True for auto-reload and easier debugging
    app.run(host="127.0.0.1", port=5000, debug=True)