
# IntelliSupport – AI-Powered Customer Support Assistant

IntelliSupport is an AI-powered customer support application that uses Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) to answer customer queries and manage support tickets.

## Features

- AI-powered customer conversations using Groq.
- RAG-based responses using FAISS and Sentence Transformers.
- Knowledge-base document retrieval.
- Support ticket creation and retrieval.
- PostgreSQL database integration using Supabase.
- REST API built with FastAPI.
- Streamlit frontend (upcoming).

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

Backend development and initial API testing completed. Streamlit frontend and public deployment are planned next.

## **Note**

This is a portfolio demonstration project. Its knowledge base contains sample support information and does not represent the policies of a real company.

