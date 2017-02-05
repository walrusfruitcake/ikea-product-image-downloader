import vcr
from downloader import image_path_scraper

def test__find_image_paths__returns_image_urls_from_slideshow():
  with vcr.use_cassette('tests/cassettes/product_page.yml'):
    url = "http://www.ikea.com/us/en/catalog/products/S29007794/"

    image_list = image_path_scraper.get_image_paths(url)

    assert len(image_list) == 8
    for image in image_list:
      assert type(image) == str
      assert image.lower().endswith((".jpg",".jpeg"))
