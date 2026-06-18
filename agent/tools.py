import os
import requests
from dotenv import load_dotenv
import yfinance as yf

load_dotenv()


def get_weather(city):

    api_key = os.getenv(
        "OPENWEATHER_API_KEY"
    )

    url = (
        "https://api.weatherapi.com/v1/current.json"
    )

    params = {
        "q": city,
        "key": api_key,
        "aqi": "no"
    }

    response = requests.get(
        url,
        params=params
    )

    data = response.json()
    # print(data)
    return {
        "city": city,
        "temperature": data["current"]["temp_c"],
        "description": data["current"]["condition"]["text"]
    }



def calculate(expression):

    try:
        result = eval(expression)
        return result

    except Exception:
        return "Invalid expression"
    

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)

    price = stock.info["currentPrice"]

    return {
        "symbol": symbol,
        "price": price
    }