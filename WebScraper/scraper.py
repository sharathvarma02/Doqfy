import yfinance as yf
import json
import redis
import time

# Redis setup
def fetch_nifty50():
    try:
        print("Fetching Nifty 50 data...")
        nifty50 = yf.Ticker("^NSEI")
        data = nifty50.history(period="1d")

        if data.empty:
            print("No data retrieved.")
            return

        nifty50_data = {
            "Date": data.index[-1].strftime("%Y-%m-%d"),
            "Open": data['Open'].iloc[-1],
            "High": data['High'].iloc[-1],
            "Low": data['Low'].iloc[-1],
            "Close": data['Close'].iloc[-1],
            "Volume": data['Volume'].iloc[-1]
        }

        print("Data fetched successfully.")
        print("Storing data in Redis...")
        r.set('nifty50', json.dumps(nifty50_data))

    except Exception as e:
        print(f"Error fetching data: {e}")

if __name__ == '__main__':
    while True:
        fetch_nifty50()
        time.sleep(300)
