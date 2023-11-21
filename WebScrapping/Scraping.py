# this file scraps the data from the web pages while iterating through the csv file.

# import requests
# from bs4 import BeautifulSoup


# page = requests.get("https://www.sebi.gov.in/rti-act-2005.html")

# soup = BeautifulSoup(page.content, "html.parser")

# print(soup.get_text())


import requests
from bs4 import BeautifulSoup
import csv

# Load URLs from CSV file
with open('C:\\Users\\DIKSHA\\Documents\\sebi.csv', 'r') as file:
    reader = csv.reader(file)
    urls = [row[0] for row in reader]

# Iterate over URLs and scrape data
for url in urls[126:130]:
    page = requests.get(url)
    
    soup = BeautifulSoup(page.content, 'html.parser')
    
    print(soup.get_text())

