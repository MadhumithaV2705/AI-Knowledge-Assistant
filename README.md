<<<<<<< HEAD
# AI Knowledge Assistant — Upgraded

## Features Added
- Semantic search with confidence scoring (color-coded %)
- 6 topic domains: Python, ML, Data Structures, Web Dev, NLP, Electronics
- Follow-up question suggestions after every answer
- Chat history with session management
- Topic sidebar with clickable filters
- Typing indicator animation
- Auto-resizing input textarea
- Clear conversation button
- REST API endpoints: /ask, /history, /topics, /clear

## Project Structure
```
AI-Knowledge-Assistant/
├── app.py
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

## Setup & Run

### Step 1 — Install dependencies
Open terminal in the project folder and run:
```
python -m pip install -r requirements.txt
```

### Step 2 — Run the app
```
python app.py
```

### Step 3 — Open browser
Go to: http://127.0.0.1:5000

## API Endpoints
| Method | Route    | Description                        |
|--------|----------|------------------------------------|
| POST   | /ask     | Ask a question, returns answer     |
| GET    | /topics  | Returns list of knowledge topics   |
| GET    | /history | Returns current session history    |
| POST   | /clear   | Clears session chat history        |

## How It Works
1. Knowledge sentences are pre-embedded at startup using MiniLM-L6-v2
2. User question is embedded in real-time
3. Cosine similarity finds the most relevant sentences
4. Confidence score shows how well the answer matches
5. Follow-up suggestions are generated based on detected topic

## What Makes It Interview-Worthy
- Real semantic search (not keyword matching)
- RESTful API design with proper status codes
- Session management
- Modular knowledge base (easy to extend)
- Confidence scoring with visual feedback
- Production-style UI with proper UX patterns
=======
# 🤖 AI Knowledge Assistant

An intelligent web-based assistant that answers user queries using **Natural Language Processing (NLP)** and **semantic similarity**. This project demonstrates how machines understand user questions and return meaningful answers from a custom knowledge base.

## 🚀 Features

* 🔍 Semantic search using sentence embeddings
* ⚡ Real-time question answering
* 🧠 NLP-based understanding (not keyword matching)
* 🌐 Simple and interactive web interface
* 📂 Custom knowledge base support

## 🛠️ Tech Stack

* **Backend:** Flask (Python)
* **NLP Model:** sentence-transformers
* **Machine Learning:** scikit-learn (cosine similarity)
* **Frontend:** HTML, CSS, JavaScript
* **Tools:** VS Code, GitHub

## 📸 Working Demo

### 🏠 Home Page

<img width="1910" height="918" alt="{5F0B8E80-B027-4839-A4ED-44DACA9B4E7A}" src="https://github.com/user-attachments/assets/c2ce3a17-4d42-42c0-89f1-55037db6524b" />

### ❓ Asking a Question

<img width="1914" height="916" alt="{4717305F-0F58-461D-96E5-1D025F578641}" src="https://github.com/user-attachments/assets/6d5fa698-dd34-4a9e-a96c-915ac67ec093" />

### 💡 Answer Output

<img width="1912" height="906" alt="{7ADFDED2-C4E5-4468-A0F1-DEB6DB9F8C59}" src="https://github.com/user-attachments/assets/95915a82-64c9-4379-9aab-07382ff9b09f" />

## ⚙️ How It Works

1. User enters a question
2. The question is converted into a numerical vector (embedding)
3. Compared with stored knowledge vectors
4. Cosine similarity finds the closest match
5. The most relevant answer is returned

## ▶️ How to Run

```bash
git clone https://github.com/MadhumithaV2705/AI-Knowledge-Assistant.git
cd AI-Knowledge-Assistant
python -m pip install -r requirements.txt
python app.py
```

Open in browser:
👉 http://127.0.0.1:5000

## 🎯 Use Cases

* 📚 **Student Learning Assistant:** Helps students quickly get answers to academic questions.
* 💬 **FAQ Automation:** Can be used to answer frequently asked questions in websites or apps.
* 🏢 **Knowledge Base Search:** Enables organizations to search internal documents efficiently.
* 🤖 **Chatbot Systems:** Can be integrated into chatbots for intelligent response generation.
* 📖 **Technical Support:** Assists users by providing solutions to common technical queries.
* 🧠 **AI-based Search Engine:** Demonstrates semantic search beyond keyword matching.
>>>>>>> 10b8c1787302fcff7120986b015bca8f2af1a520
