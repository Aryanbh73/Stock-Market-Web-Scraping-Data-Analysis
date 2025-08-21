import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                   AppleWebKit/537.36 (KHTML, like Gecko) \
                   Chrome/84.0.4147.105 Safari/537.36'
}

urls = [
    'https://groww.in/us-stocks/nke',
    'https://groww.in/us-stocks/ko', 
    'https://groww.in/us-stocks/msft', 
    'https://groww.in/stocks/m-india-ltd', 
    'https://groww.in/us-stocks/axp', 
    'https://groww.in/us-stocks/amgn', 
    'https://groww.in/us-stocks/aapl', 
    'https://groww.in/us-stocks/ba', 
    'https://groww.in/us-stocks/csco', 
    'https://groww.in/us-stocks/gs', 
    'https://groww.in/us-stocks/ibm', 
    'https://groww.in/us-stocks/intc', 
    'https://groww.in/us-stocks/jpm', 
    'https://groww.in/us-stocks/mcd',
    'https://groww.in/us-stocks/crm', 
    'https://groww.in/us-stocks/vz', 
    'https://groww.in/us-stocks/v', 
    'https://groww.in/us-stocks/wmt',  
    'https://groww.in/us-stocks/dis'
]

records = []

for url in urls:
    try:
        page = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(page.text, 'html.parser')

        company = soup.find("h1")
        company = company.get_text(strip=True) if company else "N/A"

        price = soup.find("div", {"class": "security-price"})
        price = price.get_text(strip=True) if price else "N/A"

        change = soup.find("div", {"class": "security-change"})
        change = change.get_text(strip=True) if change else "N/A"

        volume_tag = soup.find("td", string="Volume")
        volume = volume_tag.find_next("td").get_text(strip=True) if volume_tag else "N/A"

        records.append([company, price, change, volume])

        print(f"Scraped: {company}")
        time.sleep(5) 

    except Exception as e:
        print(f"Failed for {url}: {e}")

df = pd.DataFrame(records, columns=["Company", "Price", "Change", "Volume"])
df.to_excel("stocks.xlsx", index=False)
print("Saved to stocks.xlsx")
