import csv
import requests
import re
from bs4 import BeautifulSoup
result = {}
url = "http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
reponse = requests.get(url)
page = reponse.content
soup = BeautifulSoup(page, "html.parser")
book_info = soup.find_all("td")

result["title"] = soup.find('title').string.replace("\n", "").replace("| Books to Scrape - Sandbox", "").strip()
result["product_page_url"] = url
result["universal_ product_code (upc)"] = book_info[0].string
result["price_including_tax"] = book_info[3].string
result["price_excluding_tax"] = book_info[2].string
result["number_available"] = re.findall("\\d+", book_info[-2].string)
result["product_description"] = soup.find_all("p")[-1].string
result["category"] = soup.find_all("a")[-1].string
result["review_rating"] = soup.find(class_="star-rating").attrs['class'][1]
result["image_url"] = soup.find('img').attrs['src']
data = "data.csv"
with open('data.csv', 'w') as f:
    w = csv.DictWriter(f, result.keys())
    w.writeheader()
    w.writerow(result)
