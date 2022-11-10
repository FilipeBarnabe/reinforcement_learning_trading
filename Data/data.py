import yfinance as yf
import pandas as pd

def collect_data(ticker:str) -> pd.DataFrame:
    """
    This function gets a ticker and historical data
    
    ticker: can be a stock, ETF and others (example: aapl for Apple)
    """
    # Define the ticker data
    ticker = yf.Ticker(ticker)

    # Collect the data
    hist = ticker.history(period="max")

    return hist
