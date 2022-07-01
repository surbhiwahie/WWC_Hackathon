#!/usr/bin/env python
# coding: utf-8

from bs4 import BeautifulSoup as bs
from emailing_user import email
import requests
import pandas as pd
import re

url = 'http://127.0.0.1:8000/'
page = requests.get(url)
soup = bs(page.text, 'html.parser')
# print(soup.prettify())

dfs = pd.read_html(page.text)
df = dfs[0]

df = df.drop_duplicates()

#clean price field and convert to float
df["Price"] = df["Price"].str.replace("$","", regex=True)
df["Price_float"] = df["Price"].str.replace(",","", regex=True).astype('float')


#convert all postal codes and categories into lower case
postal_codes = ["M1B","M1C","M1E","M1G","M1H","M1J","M1K","M1L","M1M","M1N","M1P","M1R","M1S","M1T","M1V","M1W","M1X","M4A","M4B","M4C","M4E"]
postals = []
cat_lower = []
for p in postal_codes:
    postals.append(p.lower())

category = ['bed', 'table', 'chair', 'sofa', 'dresser','tv']
for cat in category:
    cat_lower.append(cat.lower())

postal_codes = postals
category = cat_lower

print(f"There were {df.shape[0]} posts found")

#First reducing the dataframe to search for item: Only look at items that are below a certain price
df_price_match = df[df.Price_float < 50.0]

df_price_match.loc[:,'Location'] = df_price_match.Location.str.lower()
df_price_match.loc[:,'Name'] = df_price_match.Name.str.lower()
print(f"There are {df_price_match.shape[0]} posts that are lower price")


#Capture key field values and search for an item within a postal code
for i, post in enumerate(df_price_match.Name):
    print(f"...searching {post}")
    Email_This_Person = False
    kojojo_price = df_price_match.iloc[i][2]
    kojojo_location = df_price_match.iloc[i][3]
    kojojo_item = df_price_match.iloc[i][1]
    #kojojo_email = df_price_match.iloc[i][4] 
    kojojo_email = "donationsecondchance@gmail.com"  
    kojojo_location = kojojo_location.replace(',', "")
    kojojo_location = kojojo_location.replace('-', "")
    kojojo_url = df_price_match.iloc[i][5] 
    
    for item in category:
        if(re.search(item, kojojo_item)):
            
            for i in kojojo_location.split(' '):
                if(i =="scarborough" or i in postal_codes):
                    Email_This_Person = True
    if Email_This_Person:
        print("----------------------------------------------------------------------------------------------------------------------------")
        print(f"FOUND KOJOJO USER WITH ITEM:")
        print(f"Sending email to kojojo user:{kojojo_email}! They are selling {kojojo_item} for {kojojo_price} at {kojojo_location}")
        email(kojojo_email, kojojo_url, kojojo_item)
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("\n\n")