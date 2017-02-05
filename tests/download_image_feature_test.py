import pytest
import os
import shutil
import imghdr

import download_images

@pytest.fixture
def image_dir():
  test_tree = "tests/temp"
  shutil.rmtree(test_tree, ignore_errors=True)
  # deleted one level up to force "mkdir -p" like behavior
  yield test_tree + "/downloaded_images"
  shutil.rmtree(test_tree, ignore_errors=True)

def test__download_images__populates_directory_with_images(image_dir):

  download_images.run()

  assert os.path.exists(image_dir)
  assert os.path.isdir(image_dir)
  entries = os.listdir(image_dir)
  assert len(entries) > 1
  for entry in entries:
    entry_path = os.path.join(image_dir, entry)
    assert entry_path.lower().endswith((".jpg",".jpeg"))
    assert imghdr.what(entry_path) == 'jpeg'

def test__download_images__fails_when_directory_exists(image_dir):
  os.makedirs(image_dir)

  try:
    download_images.run()
  except FileExistsError:
    return

  raise AssertionError("no FileExistsError raised")
