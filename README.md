# Rule-Based Fraud Detection with Streamlit

This project demonstrates an interpretable, rule-based system for detecting fraudulent mobile money transactions using **Python** and **Streamlit**. The system uses heuristic thresholds on transaction step duration, amount, and type to flag suspicious transactions.

mobile_transaction_fraud/
├── app/
│   └── detection.py          # Rule-based logic
├── dashboard/
│   ├── streamlit_app.py      # Rule tuner dashboard
│  
├── data/
│   └── raw/
│       └── Fraud_Analysis_Dataset.csv
└── README.md


## Features

- Interactive **rule tuning dashboard**
- Visualizations for fraud patterns by transaction type
- Real-time fraud flagging without ML model
- Manual transaction checker for custom entries
- Clean modular structure for scalability

---

## Business Use Case

Mobile money platforms face millions of transactions daily. This system helps risk analysts and fraud teams:

- Detect **high-risk transactions** in real time
- Customize thresholds with **zero training cost**
- **Explain** why a transaction is flagged (step, amount, type)
- Maintain **transparency and auditability** in fraud screening

---

## Detection Heuristics Used

The following logic is applied to identify potential frauds:

```python
# Rule-based fraud logic
IF step > STEP_THRESHOLD AND
   amount > AMOUNT_QUANTILE_THRESHOLD AND
   type IN ['TRANSFER', 'CASH_OUT']:
   → Flag as Potential Fraud

Dashboard Overview
1. Rule Tuner (Main App)
Adjust:

Step duration threshold

Amount threshold (quantile)

Allowed transaction types

See live stats:

True Positives, False Positives, etc.

Visuals:

Type distribution (all and fraud-only)

Stacked bar plots by fraud flag

2. Manual Transaction Checker
Input a single transaction manually

Get real-time fraud prediction using current rules

## How to Run
git clone https://github.com/yourusername/mobile_transaction_fraud.git
cd mobile_transaction_fraud

Create and activate virtual environment
conda create -p venv python==3.10.0
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

streamlit run dashboard/streamlit_app.py

Requirements
Python 3.9+

pandas

streamlit

matplotlib

Author
Tanvi Vishwanath
Data Scientist | ML/NLP Enthusiast | Python Developer
📍 Pune, India
🔗 LinkedIn | GitHub
