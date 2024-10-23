from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.133 Safari/537.36 Brave/114.0.5735.133",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
}



response = requests.get("https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5W4NNB/ref=sr_1_1?sr=8-1", headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

price_whole = soup.find("span", class_="a-price-whole").get_text()
print(price_whole)

