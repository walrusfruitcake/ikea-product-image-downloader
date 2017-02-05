import os
import requests

class ImageDownloader:

  def __init__(self, url_root, destination_dir):
    self.url_root = url_root
    self.destination_dir = destination_dir

  def download_image(self, source_relative_path):
    image_source_path = self.url_root + source_relative_path
    image_basename = os.path.basename(source_relative_path)
    image_destination_path = os.path.join(self.destination_dir, image_basename)

    with open(image_destination_path, 'w+b') as image_file:
      image_contents = requests.get(image_source_path).content
      image_file.write(image_contents)
