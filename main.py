import requests
import csv
from datetime import datetime

url = "https://open.er-api.com/v6/latest/PLN"

response = requests.get(url)
data = response.json()

if data["result"] != "success":
    print("API error:", data)
    exit()

rates = data["rates"]
time = datetime.now()

with open("rates.csv", "a", newline="") as file:
    writer = csv.writer(file)

    for currency, rate in rates.items():
        writer.writerow([time, "PLN", currency, rate])

print("Updated rates.csv")
