from typing import Optional
from sqlmodel import SQLModel, Field
from pydantic import BaseModel


# ── DB Table Model ──────────────────────────────────────────────
class Quote(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    quote_text: str
    author: str
    source: Optional[str] = None        # e.g. book name, movie
    category: Optional[str] = None      # e.g. motivation, wisdom
    added_at: Optional[str] = None      # string date, e.g. "2024-06-10"


# ── Request Body (Pydantic) ─────────────────────────────────────
class QuoteCreate(BaseModel):
    quote_text: str
    author: str
    source: Optional[str] = None
    category: Optional[str] = None
    added_at: Optional[str] = None


# ── Response Model ──────────────────────────────────────────────
class QuoteResponse(BaseModel):
    id: int
    quote_text: str
    author: str
    source: Optional[str]
    category: Optional[str]
    added_at: Optional[str]

    class Config:
        from_attributes = True


# ── AI Explain Response ─────────────────────────────────────────
class ExplainResponse(BaseModel):
    quote_id: int
    quote_text: str
    explanation: str