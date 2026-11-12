#!/usr/bin/env python3
"""
Write the image list for hosting a fixed set of radargrams with the picking tool.

Only needed if you want the tool to open a predefined set of images automatically
(as in the original experiment). Without an image list, users load images
themselves with the "Open images..." button.

Expected layout (repository root):

    bed_pick_annotator.html      (BASE_URL = "images/")
    images.js                    <- written here (loaded via <script>, works on file://)
    images/
      *.png | *.jpg
      images.json                <- written here (fetch fallback at BASE_URL + images.json)

File names are stored bare (no "images/" prefix); the annotator prepends BASE_URL,
so the exported CSV contains bare file names.

Usage, from the repository root:
    python make_images_json.py
or with explicit paths:
    python make_images_json.py --root path/to/site [--images-subdir images]
"""
import argparse
import json
import os

ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0].strip())
ap.add_argument("--root", default=".", help="folder containing bed_pick_annotator.html and the images subfolder")
ap.add_argument("--images-subdir", default="images", help="subfolder holding the images")
a = ap.parse_args()

img_dir = os.path.join(a.root, a.images_subdir)
if not os.path.isdir(img_dir):
    raise SystemExit("Image folder not found: %s" % img_dir)

imgs = sorted(f for f in os.listdir(img_dir) if f.lower().endswith((".png", ".jpg", ".jpeg")))
if not imgs:
    raise SystemExit("No images found in %s" % img_dir)

# images.js at the root (loaded by the <script> tag; works over file://)
with open(os.path.join(a.root, "images.js"), "w") as f:
    f.write("window.IMAGES = " + json.dumps(imgs, indent=1) + ";\n")
# images.json beside the images (fetch fallback at BASE_URL + "images.json")
with open(os.path.join(img_dir, "images.json"), "w") as f:
    json.dump(imgs, f, indent=1)

print("Wrote %s and %s (%d images)" % (os.path.join(a.root, "images.js"),
                                       os.path.join(img_dir, "images.json"), len(imgs)))
