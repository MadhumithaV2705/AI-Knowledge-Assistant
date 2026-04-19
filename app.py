from flask import Flask, request, jsonify, render_template, session
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json
import os
import uuid
from datetime import datetime

app = Flask(__name__)
app.secret_key = "ai-assistant-secret-2025"

# Load model once at startup
print("Loading AI model...")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
print("Model loaded!")

# ── Knowledge Base ──────────────────────────────────────────────────────────
knowledge_base = {
    "Python": [
        "Python is a high-level, interpreted programming language known for simplicity and readability.",
        "Python supports multiple programming paradigms including procedural, object-oriented, and functional.",
        "Python is widely used in web development, data science, machine learning, and automation.",
        "Python uses indentation to define code blocks instead of braces.",
        "Python has a rich standard library and a massive ecosystem of third-party packages via pip.",
        "Popular Python frameworks include Django and Flask for web, TensorFlow and PyTorch for ML.",
    ],
    "Machine Learning": [
        "Machine learning is a subset of AI where systems learn patterns from data without explicit programming.",
        "Supervised learning uses labeled data to train models for classification and regression tasks.",
        "Unsupervised learning finds hidden patterns in unlabeled data through clustering and dimensionality reduction.",
        "Neural networks are computational models inspired by the human brain, consisting of layers of neurons.",
        "Overfitting occurs when a model learns training data too well and fails to generalize to new data.",
        "Common ML algorithms include linear regression, decision trees, SVMs, and k-nearest neighbors.",
        "Deep learning uses multiple layers of neural networks to learn complex representations from raw data.",
    ],
    "Data Structures": [
        "Arrays store elements in contiguous memory locations and allow O(1) random access.",
        "Linked lists consist of nodes where each node contains data and a pointer to the next node.",
        "Stacks follow Last In First Out (LIFO) principle, used in function call management and undo operations.",
        "Queues follow First In First Out (FIFO) principle, used in BFS and task scheduling.",
        "Binary trees have each node with at most two children, used in search and sorting algorithms.",
        "Hash tables provide O(1) average case lookup by mapping keys to array indices using hash functions.",
        "Graphs consist of vertices and edges, used to model networks, paths, and relationships.",
    ],
    "Web Development": [
        "HTML provides the structure of web pages using semantic tags and elements.",
        "CSS controls the visual presentation and layout of web pages through selectors and properties.",
        "JavaScript adds interactivity and dynamic behavior to web pages in the browser.",
        "REST APIs use HTTP methods like GET, POST, PUT, DELETE to communicate between client and server.",
        "Flask is a lightweight Python web framework ideal for building APIs and small to medium web apps.",
        "React is a JavaScript library for building reusable UI components with a virtual DOM.",
        "HTTP status codes: 200 OK, 404 Not Found, 500 Internal Server Error, 401 Unauthorized.",
    ],
    "AI & NLP": [
        "Natural Language Processing enables computers to understand and generate human language.",
        "Word embeddings like Word2Vec and GloVe represent words as dense numerical vectors.",
        "Transformers use self-attention mechanisms to process sequential data in parallel.",
        "BERT is a pre-trained transformer model that understands context bidirectionally.",
        "Cosine similarity measures the angle between two vectors, used to find semantically similar text.",
        "Sentence transformers encode entire sentences into fixed-size vectors for semantic search.",
        "Large Language Models like GPT are trained on massive text corpora using next-token prediction.",
    ],
    "ECE / Electronics": [
        "Ohm's Law states that voltage equals current multiplied by resistance: V = IR.",
        "Capacitors store electrical energy in an electric field between two conductive plates.",
        "Inductors store energy in a magnetic field and oppose changes in current flow.",
        "MOSFETs are voltage-controlled transistors widely used in digital logic and power electronics.",
        "Operational amplifiers are high-gain differential amplifiers used in signal conditioning circuits.",
        "FPGA stands for Field Programmable Gate Array, a reconfigurable hardware chip.",
        "ADCs convert analog signals to digital, DACs convert digital signals back to analog.",
        "PCB stands for Printed Circuit Board, the substrate that interconnects electronic components.",
    ],
}

# Pre-compute embeddings for all knowledge sentences
print("Computing embeddings for knowledge base...")
all_sentences = []
all_topics = []
for topic, sentences in knowledge_base.items():
    for sentence in sentences:
        all_sentences.append(sentence)
        all_topics.append(topic)

knowledge_embeddings = model.encode(all_sentences)
print(f"Ready! {len(all_sentences)} knowledge sentences indexed.")

# In-memory chat history (per session)
chat_histories = {}

def get_best_answers(question, top_k=3):
    q_embedding = model.encode([question])
    similarities = cosine_similarity(q_embedding, knowledge_embeddings)[0]
    top_indices = np.argsort(similarities)[::-1][:top_k]

    results = []
    for idx in top_indices:
        results.append({
            "sentence": all_sentences[idx],
            "topic": all_topics[idx],
            "score": float(similarities[idx])
        })
    return results

def generate_followups(topic):
    followup_map = {
        "Python": ["What are Python decorators?", "How does Python handle memory?", "What is a Python generator?"],
        "Machine Learning": ["What is gradient descent?", "Explain overfitting and underfitting.", "What is a confusion matrix?"],
        "Data Structures": ["What is the time complexity of quicksort?", "Explain hash collisions.", "When to use a stack vs queue?"],
        "Web Development": ["How do REST APIs work?", "What is CORS?", "Explain the event loop in JavaScript."],
        "AI & NLP": ["How does BERT work?", "What are transformers?", "Explain cosine similarity."],
        "ECE / Electronics": ["What is a MOSFET?", "Explain PWM signals.", "What is an ADC?"],
    }
    return followup_map.get(topic, ["Tell me more.", "Can you explain further?", "Give me an example."])

# ── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"error": "Please enter a question."}), 400

    sid = session.get("session_id", "default")
    if sid not in chat_histories:
        chat_histories[sid] = []

    results = get_best_answers(question, top_k=3)
    top = results[0]
    confidence = top["score"]

    # Build answer
    if confidence < 0.25:
        answer = "I don't have enough information on that topic yet. Try asking about Python, Machine Learning, Data Structures, Web Development, NLP, or Electronics."
        topic = "General"
        followups = ["What is Python?", "Explain machine learning.", "What is an API?"]
    else:
        # Combine top answers if scores are close
        answer_parts = [results[0]["sentence"]]
        if len(results) > 1 and results[1]["score"] > confidence - 0.08:
            answer_parts.append(results[1]["sentence"])
        answer = " ".join(answer_parts)
        topic = top["topic"]
        followups = generate_followups(topic)

    # Save to history
    chat_histories[sid].append({
        "question": question,
        "answer": answer,
        "topic": topic,
        "confidence": round(confidence * 100, 1),
        "time": datetime.now().strftime("%H:%M")
    })

    return jsonify({
        "answer": answer,
        "topic": topic,
        "confidence": round(confidence * 100, 1),
        "followups": followups,
        "history_count": len(chat_histories[sid])
    })

@app.route("/history", methods=["GET"])
def history():
    sid = session.get("session_id", "default")
    return jsonify(chat_histories.get(sid, []))

@app.route("/topics", methods=["GET"])
def topics():
    return jsonify(list(knowledge_base.keys()))

@app.route("/clear", methods=["POST"])
def clear():
    sid = session.get("session_id", "default")
    chat_histories[sid] = []
    return jsonify({"status": "cleared"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)