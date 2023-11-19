import requests
from bs4 import BeautifulSoup
import csv

# with open('C:\\Users\\DIKSHA\\Documents\\sebi.csv','r', newline='') as f: 
#     urls = csv.reader(f)
#     # print(urls)
#     # Skip the header row if it exists
#     next(urls, None)
#     for row in urls:
#         # Assuming the URL is in the first column (index 0)
#         url = row[0]
#         page = requests.get(url)
#         soup = BeautifulSoup(page.content, "html.parser")

fileptr = open(r"C:\\Users\\DIKSHA\\Documents\\sebi.csv", "r")  
urls=fileptr.readlines()

for url in urls:
    # print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
# soup = page.content


    print(soup.get_text())
# print(soup.prettify)

# print(soup.title)



# print("\nWEBSITES\n")
# links = soup.find_all("a")
# for link in links:
#     print(link.get("href"))
