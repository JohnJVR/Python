# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 16:23:22 2020

@author: john
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
url3 = "http://olympus.realpython.org/profiles/dionysus"
page3 = urlopen(url3) # opening url
htmlsoup = page3.read().decode("utf-8")
soup = BeautifulSoup(htmlsoup,"html.parser")
print(soup.get_text())

