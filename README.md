# 📚 University Notification PDF Chatbot 🤖

## 🚀 Overview

This project implements an **AI-powered chatbot** designed to summarize university notification PDFs. Universities often release important notices and updates as lengthy PDF documents, which students may find difficult to read thoroughly. This chatbot extracts and summarizes key information from these PDFs, providing students with **concise and accessible summaries**.

Using **Retrieval-Augmented Generation (RAG)** techniques, the chatbot leverages **Natural Language Processing (NLP)** and vector search to retrieve relevant content from a repository of documents and generate clear summaries, including bullet points, key phrases, and deadlines.

---

## ✨ Features

- 🔐 **Admin Login**: Secure authentication for admins to upload and manage notification PDFs.
- 📄 **PDF Upload & Processing**: Upload PDFs, which are split into chunks, embedded using sentence transformers, and stored in Pinecone vector database.
- 🔍 **Vector Search**: Fast retrieval of relevant text chunks using Pinecone.
- 🤖 **AI-powered Chatbot**: Generates responses based on retrieved documents using Google Gemini generative AI.
- ⚡ **FastAPI Backend**: Provides API endpoints for login, uploading PDFs, and chatbot interactions.
- 🖥️ **User-Friendly Frontend**: HTML interfaces for admin login, uploading PDFs, and chatting with the bot.

---

## 🛠️ Technologies Used

- 🐍 Python 3.x
- 🚀 FastAPI (Backend API framework)
- 🗄️ MySQL (User authentication and data storage)
- 📦 Pinecone (Vector similarity search)
- 🤗 Sentence Transformers (`all-MiniLM-L6-v2`) (Text embeddings)
- 💬 Google Gemini AI (Generative AI for chatbot responses)
- 📚 Langchain (Document loaders and text splitters)
- 🎨 Jinja2 (HTML templating engine)

---

## 📁 Project Structure


├── main.py 🏗️ # FastAPI app initialization and routing

├── chatbot.py 🤖 # Chatbot logic with Pinecone & Gemini integration

├── chatbot_data_manager.py 📂 # PDF upload, processing, and Pinecone vector upsert

├── login.py 🔐 # Admin login API endpoints

├── Config/

│   └── dbconfig.py ⚙️ # MySQL database configuration

├── Schema/

│   └── all_schema.py 📋 # Pydantic schemas for request validation

├── templates/ 🖼️ # HTML templates (login.html, upload.html, index.html)

├── static/ 🎨 # Static assets (CSS, JS, images)

└── README.md 📄 # Project documentation

## 🚀 How to Run the Project: Step-by-Step Guide

### 🧱 1. Clone the Repository

git clone <your-repo-url>
cd <your-project-folder>

### 🛠️ 2. Create & Activate a Virtual Environment (Recommended)

- Create virtual environment
  
python -m venv venv

- Activate it On Windows
  
venv\Scripts\activate

- On macOS/Linux
  
source venv/bin/activate

### 📦 3. Install Required Dependencies

pip install -r requirements.txt

### ⚙️ 4. Configure the Environment

--> Edit the database configuration in Config/dbconfig.py:

-MYSQL_HOST = "localhost"

-MYSQL_USER = "your_user_name"

-MYSQL_PASSWORD = "your_password"

-MYSQL_DB = "your_db_name"

-MYSQL_PORT = 3306

--> ✅ Also, make sure to:

-Add your Pinecone and Gemini API keys in:

1.chatbot.py

2.chatbot_data_manager.py

###🚀 5. Run the FastAPI Server

uvicorn main:app --reload

--> 🌐 Open your browser and go to:

http://127.0.0.1:8000

### 🔐 6. Admin Login

-Visit: http://127.0.0.1:8000/login

-Use your admin credentials to log in

### 📤 7. Upload Notification PDFs

--> Use the upload interface to:

-✅ Upload new PDF notifications

-🗑️ Remove outdated ones

-PDFs are processed, summarized, and indexed in Pinecone for efficient retrieval

### 💬 8. Chat with the AI

--> Make a POST request to the /chatbot endpoint with JSON:

{

  "chat": "Your question about the notifications"
  
}

-The bot will respond with a clear, concise summary based on the uploaded PDFs

### 🧩 9. Customize or Extend
You can:

- 📚 Add new PDF processing logic in chatbot_data_manager.py

- 🧠 Tweak the AI prompt and logic in chatbot.py

- 🔐 Update login mechanisms in login.py

