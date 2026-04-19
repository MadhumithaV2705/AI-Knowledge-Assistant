# 🧠 AI Knowledge Assistant

An intelligent question-answering web application that uses **semantic search** and **natural language processing (NLP)** to answer queries across multiple technical domains. Built with **Python, Flask, and Sentence Transformers**.

## 📸 Preview

### 🏠 Home Page
<img width="1897" height="907" alt="{105C21F7-5EFC-4E88-8BB6-D92A870C5384}" src="https://github.com/user-attachments/assets/1ee38ade-9759-44b2-958e-807df7d0423f" />

### 📊 Answer with Confidence Score
<img width="1901" height="906" alt="{2E8B0F80-0A33-470C-85BA-55AF6A12C436}" src="https://github.com/user-attachments/assets/af9e2141-129c-41cf-82a6-92d8936a784a" />

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
