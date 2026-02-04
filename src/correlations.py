import pandas as pd

def rolling_vol_correlation(vol: pd.DataFrame, window: int = 60):
    """
    Compute rolling correlations between markets' volatilities.
    """
    corr = vol.rolling(window).corr()
    return corr
