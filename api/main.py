# api/main.py
from flask import Flask, request, jsonify
from app.detection import detect_fraud
import pandas as pd

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    
    # Example default thresholds — adjust if you want input via query or headers
    step_thresh = 10
    amount_quantile = 0.01
    allowed_types = ['TRANSFER', 'CASH_OUT']
    
    result = detect_fraud(df, step_thresh, amount_quantile, allowed_types)
    is_fraud = bool(result['isPotentialFraud'].iloc[0])
    
    return jsonify({"isPotentialFraud": is_fraud})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
