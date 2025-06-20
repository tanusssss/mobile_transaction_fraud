# app/detection.py

import pandas as pd

def detect_fraud(df, step_thresh, amount_thresh, allowed_types):
    """
    Apply rule-based logic to flag potential frauds.
    """
    some_minimum = df['amount'].quantile(amount_thresh)

    df['isPotentialFraud'] = (
        (df['step'] > step_thresh) &
        (df['amount'] > some_minimum) &
        (df['type'].isin(allowed_types))
    )

    return df
