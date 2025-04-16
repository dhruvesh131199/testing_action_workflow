# update_data.py

import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_yahoo_data(ticker):
    data = yf.download(ticker, period="1d", interval="1d")
    #data = yf.download(ticker, start = "2025-04-01", end = "2025-04-05")
    data.reset_index(inplace=True)
    data.columns = ["date", "close", "high", "low", "open", "volume"]
    data['Ticker'] = ticker
    data.head()
    return data

def update_csv(file_path, new_data):
    try:
        existing_data = pd.read_csv(file_path)
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)
        updated_data.drop_duplicates(subset=["Date", "Ticker"], inplace=True)
    except FileNotFoundError:
        updated_data = new_data

    updated_data.to_csv(file_path, index=False)

def log_run_time(log_file="run_log.txt"):
    with open(log_file, "a") as f:
        f.write(f"Script ran at: {datetime.utcnow().isoformat()} UTC\n")

def main():
    ticker = "AAPL"
    data = fetch_yahoo_data(ticker)
    update_csv("stock_data.csv", data)
    log_run_time()

if __name__ == "__main__":
    main()
