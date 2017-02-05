import pytest
import shutil
import vcr
import os
import imghdr

from downloader.image_downloader import ImageDownloader

@pytest.fixture
def test_dir():
  test_tree = "tests/temp"
  shutil.rmtree(test_tree, ignore_errors=True)
  # deleted one level up to force "mkdir -p" like behavior
  yield test_tree + "/test_dir"
  shutil.rmtree(test_tree, ignore_errors=True)

def test__download_image__downloads__when_initialized_with_url_root_and_destination_directory__and_destination_directory_exists(test_dir):
  os.makedirs(test_dir)
  with vcr.use_cassette('tests/cassettes/image_download.yml'):
    downloader = ImageDownloader("http://www.ikea.com", test_dir) 

    downloader.download_image("/PIAimages/0173711_PE327865_S5.JPG")

    downloaded_image_path = os.path.join(test_dir, "0173711_PE327865_S5.JPG")
    assert os.path.exists(downloaded_image_path)
    assert imghdr.what(downloaded_image_path) == 'jpeg'
