from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

category = ['MOVING', 'bed', 'Table', 'Chairs', 'Sofa', 'MATTRESS','tv']

postal_codes = ["M1B","M1C","M1E","M1G","M1H","M1J","M1K","M1L","M1M","M1N","M1P","M1R","M1S","M1T","M1V","M1W","M1X","M4A","M4B","M4C","M4E"]
max_price =  50

print("These are the categories we will search for:",category)
print("Focusing on Scarborough")

url = 'http://127.0.0.1:8000/'
page = requests.get(url)
soup = bs(page.text, 'html.parser')
# print(soup.prettify())
dfs = pd.read_html(page.text)
df = dfs[0]

max_price = 70
for i, post in enumerate(df.Name):
    kojojo_price = df.iloc[i][2]
    kojojo_location = df.iloc[i][3]
    kojojo_item = df.iloc[i][1]
    
    for item in category:
        #print("....Searching for ", item)
        if item in post:
            kojojo_price=kojojo_price.strip('$')
            kojojo_price_format = len(kojojo_price.split(','))

            if kojojo_price_format<4 and kojojo_price_format>1: #1,800 or 1,800,000
                pass
            else:
                #print(">>>>", item, kojojo_item)
                kojojo_price_int=int(round(float(kojojo_price.strip('$'))))

                if kojojo_price_int < max_price:
#                     print(i,"Price-Item Match for", kojojo_price, item, kojojo_location)
                    for i in kojojo_location.split(' '):
                        i = i.replace(',', "")
                        if(i == "M1T"  or i =="Scarborough"):
                            print(f"Email This person! They are selling {kojojo_item} for {kojojo_price} at  {kojojo_location}")
                            print("")