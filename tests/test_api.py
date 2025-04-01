import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database import SessionLocal, engine
from app import models

client = TestClient(app)

@pytest.fixture(scope="module")
def setup_db():
    # Create all tables
    models.Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    
    # Add test data
    bank = models.Bank(name="Test Bank")
    db.add(bank)
    db.commit()
    
    branch = models.Branch(
        name="Test Branch",
        address="123 Test St",
        city="Testville",
        district="Test District",
        state="Test State",
        bank_id=bank.id
    )
    db.add(branch)
    db.commit()
    
    yield
    
    # Clean up
    db.query(models.Branch).delete()
    db.query(models.Bank).delete()
    db.commit()
    db.close()

def test_get_banks(setup_db):
    response = client.get("/banks/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_branches(setup_db):
    response = client.get("/branches/")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_branch(setup_db):
    response = client.get("/branches/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Test Branch"

def test_get_bank_branches(setup_db):
    response = client.get("/banks/1/branches")
    assert response.status_code == 200
    assert len(response.json()) > 0