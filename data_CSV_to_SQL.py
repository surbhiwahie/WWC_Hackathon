import json
import pandas as pd
import io
import os
import requests
import datetime
import sqlalchemy
import urllib.parse
import requests

engine = sqlalchemy.create_engine('mysql://user:password@server') # connect to server
engine.execute("CREATE DATABASE dbname") #create db
engine.execute("USE dbname") # select new db

db_connection = sqlalchemy.create_engine(
    'mysql+mysqlconnector://user:pwd@hostname/db_name?auth_plugin=mysql_native_password')

## please insert the csv URL which we need to fetch the data from
url = 'https://raw.githubusercontent.com/surbhiwahie/WWC_Hackathon/main/JenAila_Furniture_Scar_ProjectPage.csv'
s= requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')), error_bad_lines=False)

## just to capture the current_datetime of the data -
Load_Date = pd.datetime.now().date()
print(Load_Date)
df['Load_Date'] = Load_Date

## we can filter it down to  multiple tables based on the category of the item:
## for this we need to add some filters and split the data into multiple dataframes
print('data loading started')
## please enter the tablename below: as of now I have taken: "wwc_furniture_data"
df.to_sql('wwc_Furniture_data', engine, if_exists='append', index=False, chunksize=1000)

print("data load completed")
