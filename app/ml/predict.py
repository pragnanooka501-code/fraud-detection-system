import joblib 
import pandas as pd

model = joblib.load(
  "app/ml/fraud_model.pkl"
)
def predict_fraud(transaction):
  
  df = pd.DataFrame([transaction])
  score =model.decisionm_function(df)[0]

  pred = model.predict(df)[0]

  return{
    "fraud" : pred == -1,
    "risk_score" : float(score)
  }