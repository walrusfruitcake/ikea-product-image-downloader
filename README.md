# Ikea Product Image Downloader

this downloader is a python 3 script to download full-size product images

### Warning

Anything in this README that implies `download_images.py` takes command-line arguments is a lie.
I am experimenting with writing a README as a spec of desired/MVP behavior.
Besides the currently-hardcoded paths, everything else should work as advertised

## but how?

To setup:

```sh
pip install -r requirements.txt
```

To run:

```sh
python download_images.py "[Ikea product URL]"
```

e.g.

```sh
python download_images.py "http://www.ikea.com/us/en/catalog/products/S29007794/"
```

To run tests

```
pip install -r requirements.txt -r test_requirements.txt
pytest
```

## but why?
I was planning to stain/paint only *part* of my Ikea Tarva frame.
To decide which part, I thought I'd open the product image and play with coloring it in GIMP.
However, the image on each product's main page is a 500x500 preview, with an underlying image that gets partially-drawn in a zoom-tool element.
So if we can get at that, we have a full-size image that's more useful for color-preview in an image manipulation program.

