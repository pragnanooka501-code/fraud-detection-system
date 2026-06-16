from fastapi import APIRouter

from app.schemas.transaction import Transaction

from app.services.fraud_services import (analyze_transaction
)
router =APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to the Fraud Detection API"}


@router.post("/predict")
def predict(transaction: Transaction):

  return analyze_transaction(
    transaction.dict()
  )