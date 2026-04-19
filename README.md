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