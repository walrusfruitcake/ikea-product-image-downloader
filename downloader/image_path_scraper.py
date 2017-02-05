import requests
from bs4 import BeautifulSoup
import re
import json

def _get_product_data(fetch_url):
  response = requests.get(fetch_url)
  assert response.status_code == 200

  soup = BeautifulSoup(response.text, "html.parser")

  def has_product_data_json(tag):
    return tag.name == "script" and "var jProductData =" in tag.text
  product_tag = soup.find(has_product_data_json)

  product_json = re.search("var jProductData = ({.*});", product_tag.text).groups()[0]
  return json.loads(product_json)

def _find_image_paths(node):
  if type(node) is dict:
    for key in node:
      if key == 'zoom':
        return node[key]
      child = _find_image_paths(node[key])
      if child is not None:
        return child
  elif type(node) is list:
    for elem in node:
      child = _find_image_paths(elem)
      if child is not None:
        return child
  else:
    return None

def get_image_paths(fetch_url):
  product_data_dict = _get_product_data(fetch_url)
  return _find_image_paths(product_data_dict)
