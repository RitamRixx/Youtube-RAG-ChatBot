# 🎥 YouTube RAG Chatbot

An AI-powered chatbot that lets you **chat with any YouTube video** using Retrieval-Augmented Generation (RAG).  
It fetches transcripts, processes them into embeddings, and allows you to ask context-aware questions.

🔗 **Live App:** https://youtube-rag-chatbot-3qj4o4h4tjyyz83xy97lgo.streamlit.app/

---

## 🚀 Features

- 📺 Extracts **YouTube video transcripts**
- 🧠 Uses **RAG (Retrieval-Augmented Generation)** for accurate answers
- 🔍 Semantic search with **vector embeddings**
- 💬 Interactive **chat interface (Streamlit)**
- ⚡ Fast and lightweight (MiniLM embeddings + GPT-4o-mini)
- 🛑 Strict grounding (answers only from video content)

---

## 🏗️ Tech Stack

- **Frontend:** Streamlit  
- **LLM:** OpenRouter (GPT-4o-mini)  
- **Embeddings:** HuggingFace (all-MiniLM-L6-v2)  
- **Vector DB:** ChromaDB  
- **Framework:** LangChain  
- **Data Source:** YouTube Transcript API  

---

## ⚙️ How It Works

1. User enters a **YouTube URL**
2. Transcript is fetched using API
3. Text is split into chunks
4. Chunks are converted into embeddings
5. Stored in **Chroma vector database**
6. User asks a question
7. Relevant chunks are retrieved
8. LLM generates answer using only context

---

## 🧪 Example Queries

- "Summarize the video in 5 points"
- "Explain the main concept simply"

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/RitamRixx/youtube-rag-chatbot.git
cd youtube-rag-chatbot
