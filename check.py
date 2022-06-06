#!/usr/bin/python

import requests
from bs4 import BeautifulSoup

r = requests.get("https://android.googlesource.com/platform/manifest/+refs").text

soup = BeautifulSoup(r, 'html.parser')

tags = soup.find_all("h3", class_="RefList-title")[1].next_sibling

for t in tags.contents:
    tag = t.text
    if "android-12.1" in tag and \
            "cts" not in tag and \
            "wear" not in tag and \
            "preview" not in tag and \
            "sdk" not in tag:
        print("Latest tag: " + tag)
        break
