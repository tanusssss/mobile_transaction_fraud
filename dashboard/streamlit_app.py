# dashboard/streamlit_app.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from app.detection import detect_fraud

# Load your data
data_path = os.path.join("data", "raw", "Fraud_Analysis_Dataset.csv")
df = pd.read_csv(data_path)

# Convert isFraud column to binary if not already
if df['isFraud'].dtype != 'int':
    df['isFraud'] = df['isFraud'].apply(lambda x: 1 if str(x).lower() == 'fraud' else 0)

st.title("Fraud Detection Rule Tuner")

# Sidebar Controls
step_thresh = st.sidebar.slider("Step Duration Threshold", min_value=7, max_value=100, value=10)
amount_quantile = st.sidebar.slider("Amount Quantile Threshold", 0.01, 0.2, 0.01)
allowed_types = st.sidebar.multiselect("Allowed Types", options=df['type'].unique(), default=['TRANSFER', 'CASH_OUT'])

# Sidebar Display Controls
show_all = st.sidebar.checkbox("Show All Transactions", value=True)
show_potential = st.sidebar.checkbox("Show Only Potential Frauds", value=True)

# Run detection
result = detect_fraud(df.copy(), step_thresh, amount_quantile, allowed_types)

# Stats
total = len(result)
frauds = result[result['isFraud'] == 1]
predicted = result[result['isPotentialFraud'] == True]
correct_preds = predicted[predicted['isFraud'] == 1]
false_negatives = frauds[~frauds.index.isin(predicted.index)]
false_positives = predicted[predicted['isFraud'] != 1]

# Display Stats
st.markdown("### 📊 Stats")
st.write(f"**Total Transactions:** {total}")
st.write(f"**Actual Frauds:** {len(frauds)}")
st.write(f"**Predicted Frauds:** {len(predicted)}")
st.write(f"**True Positives:** {len(correct_preds)}")
st.write(f"**False Positives:** {len(false_positives)}")
st.write(f"**False Negatives:** {len(false_negatives)}")



# ----------- RESULT DISPLAY -----------
st.markdown("### 📄 Filtered Transaction Results")

if show_all:
    st.subheader("All Transactions")
    st.dataframe(result[['type', 'amount', 'step', 'isFraud', 'isPotentialFraud']])

if show_potential:
    st.subheader("Potential Frauds Only")
    st.dataframe(predicted[['type', 'amount', 'step', 'isFraud', 'isPotentialFraud']])

# ----------- BAR CHARTS -----------
st.markdown("### 📈 Transaction Type Distribution")

# Convert for plotting
result['isPotentialFraud'] = result['isPotentialFraud'].astype(int)
fraud_subset = result[result['isFraud'] == 1].copy()
fraud_subset['isPotentialFraud'] = fraud_subset['isPotentialFraud'].astype(int)

# Bar 1: All Data
st.markdown("#### Full Dataset")
fig1, ax1 = plt.subplots()
pd.crosstab(result['type'], result['isPotentialFraud']).plot(kind='bar', stacked=True, ax=ax1)
ax1.set_ylabel("Count")
ax1.set_title("Potential Fraud Distribution - All Data")
st.pyplot(fig1)

# Bar 2: Fraud-Only Data
st.markdown("#### Fraud Transactions Only")
fig2, ax2 = plt.subplots()
pd.crosstab(fraud_subset['type'], fraud_subset['isPotentialFraud']).plot(kind='bar', stacked=True, ax=ax2)
ax2.set_ylabel("Count")
ax2.set_title("Potential Fraud Distribution - Fraud Data Only")
st.pyplot(fig2)