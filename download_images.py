import requests
from bs4 import BeautifulSoup
import re
import json
import os
from downloader import image_path_scraper

URL = "http://www.ikea.com/us/en/catalog/products/S29007794/"

image_dir_path = "tests/temp/downloaded_images"

def run():
  os.makedirs(image_dir_path)

  product_image_list = image_path_scraper.get_image_paths(URL)

  for image_path in product_image_list:
    base_path = os.path.basename(image_path)
    with open(os.path.join(image_dir_path, base_path), 'w+b') as image_file:
      response = requests.get("http://www.ikea.com/" + image_path)
      image_file.write(response.content)


if __name__ == "__main__":
  run()
