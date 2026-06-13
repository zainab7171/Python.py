from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from contextlib import asynccontextmanager
from groq import Groq
from dotenv import load_dotenv

from database import create_db, get_session
from schema import Quote, QuoteCreate, QuoteResponse, ExplainResponse

load_dotenv()
client = Groq()  # GROQ_API_KEY .env se read karega


# ── Groq explain function ────────────────────────────────────────
def explain_quote(quote_text: str, author: str) -> str:
    prompt = (
        f'Explain this quote in very simple, easy-to-understand words (2-3 sentences):\n\n'
        f'"{quote_text}" — {author}'
    )
    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
    )
    return response.choices[0].message.content


# ── Lifespan: create DB on startup ──────────────────────────────
@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield

app = FastAPI(
    title="📚 Quote Collection API",
    description="Save inspiring quotes and get AI explanations.",
    version="1.0.0",
    lifespan=lifespan,
)


# ── 1. POST /quotes  →  Add a new quote ─────────────────────────
@app.post("/quotes", response_model=QuoteResponse, status_code=201)
def create_quote(
    data: QuoteCreate,
    session: Session = Depends(get_session),
):
    quote = Quote(**data.model_dump())
    session.add(quote)
    session.commit()
    session.refresh(quote)
    return quote


# ── 2. GET /quotes  →  List all quotes ──────────────────────────
@app.get("/quotes", response_model=list[QuoteResponse])
def get_quotes(session: Session = Depends(get_session)):
    quotes = session.exec(select(Quote)).all()
    return quotes


# ── 3. GET /quotes/{id}  →  Get single quote ────────────────────
@app.get("/quotes/{quote_id}", response_model=QuoteResponse)
def get_quote(quote_id: int, session: Session = Depends(get_session)):
    quote = session.get(Quote, quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote


# ── 4. PUT /quotes/{id}  →  Update a quote ──────────────────────
@app.put("/quotes/{quote_id}", response_model=QuoteResponse)
def update_quote(
    quote_id: int,
    data: QuoteCreate,
    session: Session = Depends(get_session),
):
    quote = session.get(Quote, quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(quote, field, value)

    session.add(quote)
    session.commit()
    session.refresh(quote)
    return quote


# ── 5. DELETE /quotes/{id}  →  Delete a quote ───────────────────
@app.delete("/quotes/{quote_id}", status_code=204)
def delete_quote(quote_id: int, session: Session = Depends(get_session)):
    quote = session.get(Quote, quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    session.delete(quote)
    session.commit()


# ── 6. POST /quotes/{id}/explain  →  AI explains the quote ──────
@app.post("/quotes/{quote_id}/explain", response_model=ExplainResponse)
def explain(quote_id: int, session: Session = Depends(get_session)):
    quote = session.get(Quote, quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")

    explanation = explain_quote(quote.quote_text, quote.author)
    return ExplainResponse(
        quote_id=quote.id,
        quote_text=quote.quote_text,
        explanation=explanation,
    )