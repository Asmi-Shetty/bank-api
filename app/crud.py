from sqlalchemy.orm import Session

from . import models, schemas

def get_bank(db: Session, bank_id: int):
    return db.query(models.Bank).filter(models.Bank.id == bank_id).first()

def get_banks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Bank).offset(skip).limit(limit).all()

def get_branch(db: Session, branch_id: int):
    return db.query(models.Branch).filter(models.Branch.id == branch_id).first()

def get_branches(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Branch).offset(skip).limit(limit).all()

def get_branches_by_bank(db: Session, bank_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Branch).filter(models.Branch.bank_id == bank_id).offset(skip).limit(limit).all()