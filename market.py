
import requests
from config import POLYGON_API_KEY

def get_stock_price(symbol):

    url = (
        f"https://api.polygon.io/v2/aggs/ticker/"
        f"{symbol}/prev?apiKey={POLYGON_API_KEY}"
    )

    try:
        response = requests.get(url).json()

        if "results" in response:
            return response["results"][0]["c"]

    except Exception:
        return None

    return None
