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
