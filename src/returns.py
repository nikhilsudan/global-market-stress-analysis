import pandas as pd

def compute_returns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Compute daily percentage returns from aligned price data.

    Parameters
    ----------
    prices : DataFrame
        Aligned prices with Date index and columns:
        ['NIFTY 50', 'S&P 500', 'FTSE 100']

    Returns
    -------
    DataFrame
        Daily percentage returns.
    """
    returns = prices.pct_change().dropna()
    return returns
