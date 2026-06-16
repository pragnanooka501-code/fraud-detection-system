from app.ml.predict import predict_fraud

def analyze_transaction(data):
  result=predict_fraud(data)

  return result