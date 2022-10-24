import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.amazon.com/Logitech-Dual-motor-Feedback-Responsive-PlayStation/dp/B00Z0UWWYC/ref=zg_bs_7926841011_28/136-1595290-3211209?pd_rd_i=B00Z0UWWYC&psc=1"

headers = {
"Access-Language": "en-US,en;q=0.5",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0"
}

response = requests.get(url, headers=headers)
website = response.text

soup = BeautifulSoup(website, "lxml")
data = soup.find(name="span", class_="a-offscreen")
price = data.text
print(price)