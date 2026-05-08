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


time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

file_name = "rates.csv"


with open(file_name, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)


    writer.writerow(["timestamp", "base_currency", "currency", "rate"])

    for currency, rate in rates.items():
        writer.writerow([time, "PLN", currency, rate])

print("Updated rates.csv")
