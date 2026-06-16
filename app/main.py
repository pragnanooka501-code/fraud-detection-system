from fastapi import FastAPI
from app.api.predict import router

app=FastAPI(
  title="Fraud Dtetection API"
)

app.include_router(router)
