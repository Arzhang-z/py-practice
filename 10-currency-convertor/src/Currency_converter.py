import requests
import os
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=3*60*60)



@cached(cache=cache)
def get_exchange_rate(base_currency: str = "CAD", target_currency: str = "USD") -> float:
    try:
        YOUR_Exchange_Rate_API_KEY = os.environ['YOUR_Exchange_Rate_API_KEY']
        if not YOUR_Exchange_Rate_API_KEY:
            raise RuntimeError("Exchange Rate API key not set")
        
        url = f'https://v6.exchangerate-api.com/v6/{YOUR_Exchange_Rate_API_KEY}/latest/{base_currency}'
    
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        return data['conversion_rates'][target_currency]
    
    except requests.exceptions.Timeout:
        raise RuntimeError("Exchange Rate API timed out")

    except requests.exceptions.HTTPError as e:
        raise RuntimeError(f"HTTP error from Exchange Rate API: {e}")
    
    except KeyError:
        raise RuntimeError(f"Invalid Currency code: {target_currency}")
    
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Network error: {e}")


def convert_currency(amount: float = 100.0, exchange_rate: float = 1.0) -> float:
    if exchange_rate is None:
        raise ValueError("Exchange rate is None")
    return amount * exchange_rate


if __name__ == "__main__":
    try:
        base_currency = input("Enter base currency: ").upper()
        target_currency = input("Enter Target Currency: ").upper()
        amount = float(input("Enter amount: "))
    
        exchange_rate = get_exchange_rate(base_currency, target_currency)
        convert_amount = convert_currency(amount, exchange_rate)
    
        print(f"{amount} {base_currency} is {convert_amount} {target_currency}")
    
    except Exception as e:
        print(f"Error: {e}")
