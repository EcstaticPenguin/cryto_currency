import requests
from bs4 import BeautifulSoup

while True:
    crypto_currency = input("\nenter the name of cryptocurrency-->").lower()
    response = requests.get(f"https://gadgets.ndtv.com/finance/{crypto_currency}-price-in-india-today-inr")
    webpage = response.text

    soup = BeautifulSoup(webpage, "html.parser")
    print(f"\ncurrent rate of {crypto_currency} is -->",soup.find_all("span")[2].getText(),"\n")

    x = input("press C to continue searching or E to exit-->").lower()
    if x == "e":
        break
    elif x != "c":
        break
