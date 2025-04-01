from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import SessionLocal, engine

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Bank Branch API",
    description="API for accessing bank and branch information",
    version="1.0.0",
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/banks/", response_model=list[schemas.Bank])
def get_banks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get list of all banks"""
    banks = crud.get_banks(db, skip=skip, limit=limit)
    return banks

@app.get("/branches/", response_model=list[schemas.Branch])
def get_branches(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get list of all branches"""
    branches = crud.get_branches(db, skip=skip, limit=limit)
    return branches

@app.get("/branches/{branch_id}", response_model=schemas.BranchDetail)
def get_branch(branch_id: int, db: Session = Depends(get_db)):
    """Get details of a specific branch"""
    branch = crud.get_branch(db, branch_id=branch_id)
    if branch is None:
        raise HTTPException(status_code=404, detail="Branch not found")
    return branch

@app.get("/banks/{bank_id}/branches", response_model=list[schemas.Branch])
def get_bank_branches(bank_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all branches for a specific bank"""
    branches = crud.get_branches_by_bank(db, bank_id=bank_id, skip=skip, limit=limit)
    return branches