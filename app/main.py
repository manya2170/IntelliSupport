
from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import SQLAlchemyError

from app.database.database import Base, engine, SessionLocal
from app.database.models import Ticket
from app.schemas import TicketCreate, TicketResponse, ChatRequest

from app.services.ai_service import generate_ai_response
from app.services.rag_service import generate_rag_response


# Initialize FastAPI
app = FastAPI(
    title="IntelliSupport API",
    description="AI-powered Customer Support Assistant",
    version="1.0.0"
)


# Create database tables if they do not exist
Base.metadata.create_all(bind=engine)


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to IntelliSupport!",
        "status": "Running"
    }


# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}


# Create a new support ticket
@app.post(
    "/tickets",
    response_model=TicketResponse,
    status_code=201
)
def create_ticket(ticket: TicketCreate):

    try:
        with SessionLocal() as session:

            new_ticket = Ticket(
                customer_name=ticket.customer_name,
                email=str(ticket.email),
                message=ticket.message
            )

            session.add(new_ticket)
            session.commit()
            session.refresh(new_ticket)

            return new_ticket

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Unable to create support ticket."
        )


# Retrieve all support tickets
@app.get("/tickets", response_model=list[TicketResponse])
def get_tickets():

    try:
        with SessionLocal() as session:
            return session.query(Ticket).order_by(
                Ticket.created_at.desc()
            ).all()

    except SQLAlchemyError:
        raise HTTPException(
            status_code=500,
            detail="Unable to retrieve support tickets."
        )


# Basic AI chat endpoint
@app.post("/chat")
def chat(request: ChatRequest):

    response = generate_ai_response(request.message)

    return {
        "customer_message": request.message,
        "assistant_response": response,
        "mode": "AI"
    }


# Retrieval-Augmented Generation endpoint
@app.post("/rag-chat")
def rag_chat(request: ChatRequest):

    response = generate_rag_response(request.message)

    return {
        "customer_message": request.message,
        "assistant_response": response,
        "mode": "RAG"
    }
