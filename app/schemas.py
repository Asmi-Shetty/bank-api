from typing import Optional
from pydantic import BaseModel

class BankBase(BaseModel):
    name: str

class BankCreate(BankBase):
    pass

class Bank(BankBase):
    id: int
    
    class Config:
        orm_mode = True

class BranchBase(BaseModel):
    name: str
    address: str
    city: str
    district: str
    state: str

class BranchCreate(BranchBase):
    bank_id: int

class Branch(BranchBase):
    id: int
    bank_id: int
    
    class Config:
        orm_mode = True

class BranchDetail(Branch):
    bank: Bank
    
    class Config:
        orm_mode = True