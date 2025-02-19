import requests
from django.conf import settings

# Module-level variable to hold the gold price once fetched
GLOBAL_GOLD_PRICE = None

class GoldPriceRetrievalError(Exception):
    """Custom exception for gold price retrieval errors."""
    pass

def get_current_gold_price():
    """
    Retrieves the current price per gram of pure gold in US dollars.
    Fetches the gold price only once; subsequent calls return the stored value.
    Raises a GoldPriceRetrievalError if the API call fails.
    """
    global GLOBAL_GOLD_PRICE
    # If we already have a value, return it
    if GLOBAL_GOLD_PRICE is not None:
        return GLOBAL_GOLD_PRICE

    url = 'https://www.goldapi.io/api/XAU/USD'
    headers = {
        'x-access-token': settings.GOLD_API_KEY,
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        gold_price = data.get('price_gram_24k')
        if gold_price is None:
            raise GoldPriceRetrievalError(f"Gold price not found in API response: {data}")
        # Save the fetched gold price to our global variable
        GLOBAL_GOLD_PRICE = gold_price
        return GLOBAL_GOLD_PRICE
    except Exception as e:
        raise GoldPriceRetrievalError(f"Error retrieving gold price: {e}")
