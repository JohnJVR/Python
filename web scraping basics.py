# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 15:18:44 2020

@author: john
"""
from urllib.request import urlopen

url1 = "http://olympus.realpython.org/profiles/poseidon"
page1 = urlopen(url1)
html_bytes1 = page1.read() # reading url page
# decoding with utf-8 (it convert from sequence bytes to sequence of character )
html1 = html_bytes1.decode("utf-8")
print(html1) # checking what are the details that we collected from HTML
html_index1 = html1.find("<title>")
html_index1 # find index of opening tag
start_index1 = html_index1+len("<title>")
start_index1 
end_index1 = html1.find("<title>")
end_index1
title1 = html1[start_index1:end_index1]
title1

