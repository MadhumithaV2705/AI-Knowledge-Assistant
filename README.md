# 🧠 AskIQ — Semantic Intelligence Assistant

An intelligent question-answering web application that uses **semantic search** and **natural language processing (NLP)** to answer queries across multiple technical domains. Built with **Python, Flask, and Sentence Transformers**.

## 📸 Preview

### 🏠 Home Page
<img width="1904" height="905" alt="{5DB2FCEC-FDA2-4930-AED4-53C1703C64EB}" src="https://github.com/user-attachments/assets/34493025-f41d-4995-bd6b-d86723d3e197" />

### 📊 Answer with Confidence Score
<img width="1909" height="900" alt="{A0DD1089-3B96-4A06-B2D0-8B2D6A97245F}" src="https://github.com/user-attachments/assets/a8d81011-a3d9-48c7-ac93-cd1ee66afae1" />

## 🚀 Features

- 🔍 Semantic search (meaning-based, not keyword-based)
- 📊 Confidence scoring with color indicators
- 🗂️ 6 knowledge domains (Python, ML, DS, Web, NLP, Electronics)
- 💡 Follow-up question suggestions
- 🌐 REST API endpoints
- 📱 Responsive design

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **AI Model:** sentence-transformers (all-MiniLM-L6-v2)  
- **Similarity:** Cosine similarity (scikit-learn)  
- **Frontend:** HTML, CSS, JavaScript  
- **Processing:** NumPy  

## 🧠 How It Works

1. User enters a question  
2. Question is converted into a vector (embedding)  
3. Compared with precomputed knowledge embeddings  
4. Cosine similarity finds the best match  
5. Answer is returned with confidence score and follow-up suggestions  

## ⚙️ Setup & Run

```bash
git clone https://github.com/MadhumithaV2705/AI-Knowledge-Assistant.git
cd AI-Knowledge-Assistant
python -m pip install -r requirements.txt
python app.py
```
## 🌐 Access the Application
```
👉 http://127.0.0.1:5000
```

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | /ask     | Ask a question |
| GET    | /topics  | Get all topics |
| GET    | /history | Get chat history |
| POST   | /clear   | Clear chat |

## 📊 Sample Response

```json
{
  "answer": "Python is a high-level programming language...",
  "topic": "Python",
  "confidence": 87.4,
  "followups": [
    "What are Python decorators?",
    "How does Python handle memory?"
  ]
}
```

## 🎯 Use Cases

- Student learning assistant  
- FAQ automation  
- Knowledge base search  
- Chatbot backend  
- Technical support system  

## 💡 Key Highlights

- Real semantic search (not keyword-based)  
- NLP using sentence embeddings  
- Cosine similarity for accurate matching  
- REST API design with Flask  
- Clean frontend + backend integration  

## 🔮 Future Improvements

- Add PDF/document upload  
- Integrate LLM APIs  
- Cloud deployment  
- User authentication  
- Expand knowledge domains  

## ⭐ Conclusion

This project demonstrates a practical implementation of **semantic search and NLP** to build an intelligent, real-time question-answering system. It highlights strong understanding of **AI concepts, backend development, and full-stack integration**, making it a solid **interview-ready project**.
