import pandas as pd

def compute_drawdowns(prices: pd.DataFrame) -> pd.DataFrame:
    """
    Compute path-dependent drawdowns for each market.

    Drawdown_t = (Price_t / Historical Peak_t) - 1

    Parameters
    ----------
    prices : DataFrame
        Aligned price data with Date index.

    Returns
    -------
    DataFrame
        Drawdowns (negative values).
    """

    running_max = prices.cummax()
    drawdowns = prices / running_max - 1

    return drawdowns
