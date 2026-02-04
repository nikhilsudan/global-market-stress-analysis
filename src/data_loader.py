import pandas as pd

def load_single_csv(path, price_name):
    """
    Load one Yahoo Finance-style CSV, parse Date, keep the price column,
    clean it, convert to numeric, and rename it to a clean market name.
    """

    # Read raw CSV
    df = pd.read_csv(path)

    # ---- DATE HANDLING ----
    df["Date"] = pd.to_datetime(df["Date"], format="mixed", errors="coerce")
    df = df.dropna(subset=["Date"])   # drop rows with invalid dates

    # ---- IDENTIFY PRICE COLUMN ----
    # Your files use "Price". We still keep a fallback for "Close".
    if "Price" in df.columns:
        price_col = "Price"
    else:
        price_col = [c for c in df.columns if "Close" in c][0]

    # ---- KEEP ONLY WHAT WE NEED ----
    df = df[["Date", price_col]].copy()

    # ---- CLEAN & CONVERT PRICES ----
    # Removes commas like "19,452.35" and converts to float
    df[price_col] = (
        df[price_col]
        .astype(str)
        .str.replace(",", "", regex=False)
        .astype(float)
    )

    # ---- RENAME AND INDEX ----
    df = df.rename(columns={price_col: price_name})
    df = df.set_index("Date")

    return df


def load_aligned_prices(nifty_path, spx_path, ftse_path):
    """
    Load all three markets and align to common trading days.
    Returns one dataframe with columns:
    ['NIFTY 50', 'S&P 500', 'FTSE 100']
    """

    nifty = load_single_csv(nifty_path, "NIFTY 50")
    spx = load_single_csv(spx_path, "S&P 500")
    ftse = load_single_csv(ftse_path, "FTSE 100")

    # Inner join keeps only dates present in all three markets
    prices = nifty.join([spx, ftse], how="inner")

    return prices
