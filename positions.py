import requests
import json

URL = "https://paper-trading.lemon.markets/v1/positions/"
API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJsZW1vbi5tYXJrZXRzIiwiaXNzIjoibGVtb24ubWFya2V0cyIsInN1YiI6InVzcl9xeUdQUkNDOTlZTEh3blFUbnlscURjblB5ZHpzTnNac0w5IiwiZXhwIjoxNjU1MDQ4ODgxLCJpYXQiOjE2NDk4NjQ4ODEsImp0aSI6ImFwa19xeUdSVDc3RERNTGZiUVhXVnRTS2N0a3IzWkZUNnpod1REIiwibW9kZSI6InBhcGVyIn0.yEHvIFrd_DjcC_vfKLZrJtfssHCUT0EGOk6cm70WRrw"


request = requests.get("https://paper-trading.lemon.markets/v1/positions/", 
                       headers={"Authorization": "Bearer " + API_KEY})

r = request.json()
results = r["results"]


class Aktie():
    def __init__(self, isin, isin_title, quantity, buy_price_avg, estimated_price, estimated_price_total):
        self.isin = isin
        self.isin_title = isin_title
        self.quantity = quantity
        self.buy_price_avg = buy_price_avg
        self.estimated_price = estimated_price
        self.estimated_price_total = estimated_price_total

    # def estimated_price_total():
    #     return quantity*estimated_price

aktien = []
count = 0
counter = []

total_investment = 0

for result in results:
    isin = result["isin"]
    isin_title = result["isin_title"]
    quantity = result["quantity"]
    buy_price_avg = result["buy_price_avg"]
    estimated_price = result["estimated_price"]
    estimated_price_total = result["estimated_price_total"]

    # total_investment = buy_price_avg * quantity
    # total_investment_capital += total_investment

    total_investment += estimated_price_total

    aktie = Aktie(isin, isin_title, quantity, buy_price_avg, estimated_price, estimated_price_total) 
    aktien.append(aktie)

    count += 1
    counter.append(count)


print(type(total_investment))
print(total_investment)
total_investment = str(total_investment)
total_investment = total_investment[:3] + "." + total_investment[3:]
total_investment = float(total_investment)
total_investment = "€" + str(total_investment)
print(total_investment)

# total_investment = str(total_investment)
# total_investment = "€" + total_investment[:3] + "," + total_investment[3:]

