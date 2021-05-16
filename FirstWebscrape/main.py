from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
import csv

my_url = 'https://store.steampowered.com/search/?sort_by=Released_DESC&tags=128'
# opening connection, grabbing the page
uClient = ureq(my_url)
page_html = uClient.read()
# opening connection
uClient.close()

# html parsing
page_soup = soup(page_html.decode("utf-8"), "html.parser")

# grabs each product
divs = page_soup.findAll("a", {"class": "search_result_row"})

filename = "steam.csv"
outfilehandle = csv.writer(open('steam.csv', 'w', encoding='utf-8'))
f = open(filename, "w")
headers = "Title, Price\n"
f.write(headers)

for container in divs:
    title = container.findAll("span", {"class": "title"})
    product_name = title[0].text.encode().decode()
    price = container.findAll("div", {"class": "search_price"})
    product_price = price[0].text.strip()

    outfilehandle.writerow([product_name] + [product_price])

f.close()
