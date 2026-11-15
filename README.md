
# IntelliSupport – AI-Powered Customer Support Assistant

Live Demo: https://intellisupport-6bgeuccamdpwlagc6muegx.streamlit.app/

IntelliSupport is an AI-powered customer support application that uses Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) to answer customer queries and manage support tickets.

## Features

- AI-powered customer conversations using Groq.
- RAG-based responses using FAISS and Sentence Transformers.
- Knowledge-base document retrieval.
- Support ticket creation and retrieval.
- PostgreSQL database integration using Supabase.
- REST API built with FastAPI.
- Streamlit frontend deployed on Streamlit Community Cloud.
  
## Tech Stack

- Python
- FastAPI
- Groq API
- Sentence Transformers
- FAISS
- PostgreSQL
- Supabase
- SQLAlchemy
- Streamlit

## Project Structure

```text
IntelliSupport/
├── app/
│   ├── main.py
│   ├── schemas.py
│   ├── database/
│   ├── services/
│   └── knowledge_base/
├── requirements.txt
├── .gitignore
├── .env.example
└── README.
```

## Setup

1. Clone the repository.

2. Install dependencies:

   bash
   pip install -r requirements.txt

3. Configure SUPABASE_DB_URL and GROQ_API_KEY as environment variables.
4. Start the FastAPI application:


   uvicorn app.main:app --reload
5. Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to explore the API.

## **Project Status**

Successfully developed and deployed. The Streamlit frontend is live, the FastAPI backend is integrated, and the application is publicly accessible. Core features include AI-powered support, RAG-based responses, and Supabase ticket management.

## **Note**

This is a portfolio demonstration project. Its knowledge base contains sample support information and does not represent the policies of a real company.

