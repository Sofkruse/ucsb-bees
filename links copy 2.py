#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 21:51:05 2023

@author: sofiakruse
"""
import pip
from bs4 import BeautifulSoup
import requests
import wikipedia
native_wiki_page = requests.get(
    "https://en.wikipedia.org/wiki/List_of_California_native_plants")
# got webpage with requests
print(native_wiki_page.status_code)
print(native_wiki_page.content)
# start to go through it
soup = BeautifulSoup(native_wiki_page.content, 'html.parser')
print(soup.prettify())
alllinks = soup.find(id="mw-content-text").find_all("a")

for link in alllinks:
    if link['href'].find("/wiki/") == -1: 
        continue
# href for links 
    linktoscrape = link
    break

# href for links 
    linktoscrape = link
    break

print(link.prettify())

titles = wikipedia.page("List of California Native Plants").links
print(titles)

categories1 = wikipedia.page("List of California Native Plants").categories
print(categories1)


# %pip install clean-text to console
# title is fancier name, text and textContent is normal






# at this point, scraped all links





# when find do vector to get name and location at the same time
