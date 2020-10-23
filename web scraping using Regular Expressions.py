# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:43:12 2020

@author: john
"""
import re
from urllib.request import urlopen

url2 = "http://olympus.realpython.org/profiles/aphrodite"
page3 = urlopen(url2)
html2 = page3.read().decode("utf-8")
# For regular expressions pattern will be in a handy
pattern = "<title.*?,*?</title.*?>"
match_results = re.search(pattern,html2, re.IGNORECASE)
title2 = match_results.group()
title2 = re.sub("<.*?", "",title2)# it removes html tag
print(title2)

