# ShopPH API

Used by: **[FastAPI guide](../../fastapi/fastapi_learning_guide.html)**

**Not a downloadable dataset.** ShopPH is a Philippine e-commerce REST API the learner builds module-by-module — the guide's exercises *are* the implementation, so no starter code is provided here.

## Stack

- Framework: FastAPI + Uvicorn
- Validation: Pydantic
- ORM: SQLAlchemy
- Auth: JWT

## Starting shape (Module 1.1)

```python
from fastapi import FastAPI

app = FastAPI(
    title="ShopPH API",
    description="Philippine e-commerce platform API",
    version="1.0.0",
)

@app.get("/")
async def root() -> dict:
    return {"message": "Welcome to ShopPH API", "docs": "/docs"}

@app.get("/health")
async def health_check() -> dict:
    return {"status": "ok", "service": "shopph-api"}
```

Run with `uvicorn main:app --reload`; Swagger UI is auto-generated at `/docs`, ReDoc at `/redoc`.

## Domain

Products, users, orders, and authentication — the guide builds these out module by module (routing → Pydantic schemas → SQLAlchemy models → auth middleware → testing → deployment), ending in a production-hardened API (Phase 3 Capstone: **Production ShopPH API**).

## Notes

- If you want a matching database instead of building the schema from scratch, [`tindahub/`](../tindahub/) (used by the PostgreSQL & Metabase guide) has a compatible products/customers/orders shape you can adapt — same Philippine e-commerce domain, already normalized with `CHECK` constraints.
