# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 20:30:59 2020

@author: William Stencel
"""
from bs4 import BeautifulSoup  # Parsing HTML
import requests  # Internet information requests
#import re        # Regular Expressions (Regex) package

htmlPath = 'http://publicinterestlegal.org/county-list/'
htmlDoc = requests.get(htmlPath, headers={'User-Agent': 'Mozilla/5.0'}).content # was getting 403 error

""" parse html """
htmlParsed = BeautifulSoup(htmlDoc, 'lxml')
counties = htmlParsed.find_all('tr')  # Finds one row of data


county_tbl = []  # set up an empty list in which to store the data 
for county in counties:
    new_county = []   #create empty list to store the data from the next county
    for field in county.find_all('td'): 
        new_county.append(field.text)   # append next data point to the current county list
        
    county_tbl.append(new_county)        # append current county data list to overall list

print('\nWSSTENCEL')
print('Number of sublists in results using len() function: ', len(county_tbl), '\n\n')
print(county_tbl)

