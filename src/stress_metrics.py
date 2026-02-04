import pandas as pd
import numpy as np

def compute_spx_vol_threshold(spx_vol: pd.Series, percentile: float = 80) -> float:
    """
    Compute the turbulence threshold as the 80th percentile
    of S&P 500 rolling volatility over the full sample.

    Returns a single scalar threshold.
    """
    return np.nanpercentile(spx_vol, percentile)


def label_turbulence(spx_vol: pd.Series, threshold: float) -> pd.Series:
    """
    Label each day as:
      1 = Turbulent (volatility above threshold)
      0 = Calm      (volatility at or below threshold)

    Returns a Series of 0/1 with same index as spx_vol.
    """
    turbulence = (spx_vol > threshold).astype(int)
    return turbulence


def compute_sensitivity_score(local_vol: pd.Series,
                              spx_vol: pd.Series,
                              turbulence: pd.Series) -> float:
    """
    Compute Market Sensitivity Score:

    Sensitivity =
        (Average change in local volatility during turbulent periods)
        ---------------------------------------------------------------
        (Average change in S&P volatility during turbulent periods)

    Steps:
    1) Compute day-to-day changes in volatility.
    2) Keep only turbulent days.
    3) Take mean absolute change for both markets.
    4) Return ratio.
    """

    # Day-to-day changes in volatility
    local_change = local_vol.diff().abs()
    spx_change = spx_vol.diff().abs()

    # Keep only turbulent days
    local_turb = local_change[turbulence == 1]
    spx_turb = spx_change[turbulence == 1]

    # Avoid division by zero
    if spx_turb.mean() == 0 or np.isnan(spx_turb.mean()):
        return np.nan

    sensitivity = local_turb.mean() / spx_turb.mean()
    return float(sensitivity)
