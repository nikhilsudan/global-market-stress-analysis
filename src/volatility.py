import pandas as pd
import numpy as np

def rolling_annualized_vol(returns: pd.DataFrame, window: int = 30) -> pd.DataFrame:
    """
    Compute 30-day rolling annualized volatility.

    Vol_t = sqrt(252) * rolling_std(returns, window)

    Parameters
    ----------
    returns : DataFrame
        Daily percentage returns with Date index.
    window : int
        Rolling window in trading days (default = 30).

    Returns
    -------
    DataFrame
        Rolling annualized volatility.
    """
    vol = returns.rolling(window).std() * np.sqrt(252)
    return vol
