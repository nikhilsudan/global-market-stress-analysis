import pandas as pd
import numpy as np

def train_test_split(vol: pd.DataFrame):
    """
    Split volatility into:
    - Train: 2020–2024
    - Test: 2025

    Uses explicit year filtering (robust to gaps and non-monotonic indexes).
    """

    vol_sorted = vol.sort_index().copy()

    years = vol_sorted.index.year

    train = vol_sorted[years <= 2024]
    test = vol_sorted[years == 2025]

    return train, test


def fit_ar1_forecast(train_series: pd.Series, test_series: pd.Series):
    """
    Fit a simple AR(1) model:
        Vol_{t+1} = alpha + beta * Vol_t

    IMPORTANT: This version uses *pure recursive forecasting* for 2025
    (no peeking at actual values during prediction).
    """

    # Drop NaNs from rolling window start
    y = train_series.dropna()

    # Prepare X = Vol_t, Y = Vol_{t+1}
    X = y.shift(1).dropna()
    Y = y.loc[X.index]

    # Estimate alpha, beta via OLS
    X_mat = np.column_stack([np.ones(len(X)), X])
    params = np.linalg.lstsq(X_mat, Y, rcond=None)[0]
    alpha, beta = params[0], params[1]

    # --- PURE FORWARD FORECAST FOR 2025 ---
    preds = []
    last_vol = y.iloc[-1]  # last known 2024 volatility

    for _ in range(len(test_series)):
        pred = alpha + beta * last_vol
        preds.append(pred)
        last_vol = pred   # <-- NOW we feed back the PREDICTION

    preds = pd.Series(preds, index=test_series.index)

    return (alpha, beta), preds



def evaluate_forecast(actual: pd.Series, predicted: pd.Series):
    """
    Compute RMSE and MAE for forecast evaluation.
    """

    df = pd.concat([actual, predicted], axis=1, join="inner")
    df.columns = ["actual", "pred"]

    errors = df["actual"] - df["pred"]

    rmse = float(np.sqrt((errors**2).mean()))
    mae = float(errors.abs().mean())

    return rmse, mae
