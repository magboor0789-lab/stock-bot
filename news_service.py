
import requests
from config import FINNHUB_API_KEY

def get_news(symbol):

    url = (
        f"https://finnhub.io/api/v1/company-news?"
        f"symbol={symbol}"
        f"&from=2026-01-01"
        f"&to=2026-12-31"
        f"&token={FINNHUB_API_KEY}"
    )

    try:
        data = requests.get(url).json()

        headlines = []

        for item in data[:5]:
            headlines.append(item.get("headline"))

        return headlines

    except Exception:
        return []
