import pandas as pd
import numpy as np

def make_lag_features(vol: pd.Series, lags=[1, 5]):
    """
    Create simple lag features for ML:
      Vol_t, Vol_{t-5}
    """
    df = pd.DataFrame({
        "vol": vol,
        "lag_1": vol.shift(1),
        "lag_5": vol.shift(5)
    }).dropna()

    X = df[["lag_1", "lag_5"]]
    y = df["vol"]

    return X, y


def fit_lag_regression(train_vol: pd.Series, test_vol: pd.Series):
    """
    Fit: Vol_{t+1} = a + b1*Vol_t + b2*Vol_{t-5}
    Uses closed-form OLS (no sklearn needed).
    """

    # Build features on train
    X_train, y_train = make_lag_features(train_vol)

    # Add constant term
    X_mat = np.column_stack([
        np.ones(len(X_train)),
        X_train.values
    ])

    # OLS solution
    params = np.linalg.lstsq(X_mat, y_train.values, rcond=None)[0]
    alpha, beta1, beta5 = params

    # Build features on test (aligned)
    X_test, _ = make_lag_features(test_vol)

    X_test_mat = np.column_stack([
        np.ones(len(X_test)),
        X_test.values
    ])

    preds = pd.Series(
        X_test_mat @ params,
        index=X_test.index
    )

    return (alpha, beta1, beta5), preds


def evaluate_forecast(actual: pd.Series, predicted: pd.Series):
    """
    Same metrics as your AR(1) benchmark.
    """
    df = pd.concat([actual, predicted], axis=1, join="inner")
    df.columns = ["actual", "pred"]

    errors = df["actual"] - df["pred"]

    rmse = float(np.sqrt((errors**2).mean()))
    mae = float(errors.abs().mean())

    return rmse, mae
