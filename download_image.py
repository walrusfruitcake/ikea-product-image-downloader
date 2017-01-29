import requests
from bs4 import BeautifulSoup
import re
import json

URL = "http://www.ikea.com/us/en/catalog/products/S29007794/"

response = requests.get(URL)
assert response.status_code == 200

soup = BeautifulSoup(response.text, "html.parser")


def has_product_data_json(tag):
  return tag.name == "script" and "var jProductData =" in tag.text

product_tag = soup.find(has_product_data_json)
product_json = re.search("var jProductData = ({.*});", product_tag.text).groups()[0]
product_data = json.loads(product_json)

print(product_data)
