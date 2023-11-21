# This file basically creates the csv file which is then been used to access for web scraping

import requests
from bs4 import BeautifulSoup
import csv

urls = [
        "https://www.sebi.gov.in/",
        "https://www.sebi.gov.in/about.html",
        "https://www.sebi.gov.in/legal.html",
        "https://www.sebi.gov.in/enforcement.html",
        "https://www.sebi.gov.in/filings.html",
        "https://www.sebi.gov.in/reports-and-statistics.html",
        "https://www.sebi.gov.in/status.html",
        "https://www.sebi.gov.in/media-and-notifications.html" ]

with open('C:\\Users\\DIKSHA\\Documents\\sebi.csv', 'a', newline='\n') as f:
    writer = csv.writer(f)

    for url in urls:
        writer.writerow([url])

        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        base = "https://www.sebi.gov.in/"

        # Find links with class "list_item_inner"
        links_list_item_inner = soup.find_all("a", class_="list_item_inner")

        for link_list_item_inner in links_list_item_inner:
            
            if "https" in link_list_item_inner.get("href"):
                full_url_list_item_inner = link_list_item_inner.get("href")
                print(full_url_list_item_inner)
            else:
                #Construct the full URL by assuming links are relative paths
                full_url_list_item_inner = f"{base}{link_list_item_inner.get('href')}"

            # Access the page with class "list_item_inner"
            page_list_item_inner = requests.get(full_url_list_item_inner)
            soup_list_item_inner = BeautifulSoup(page_list_item_inner.content, "html.parser")

            # Find links with class "points" on the page with class "list_item_inner"
            links_points = soup_list_item_inner.find_all("a", class_="points")

            for link_points in links_points:
                    full_url_points = link_points.get("href")
                    print(full_url_points)
                    writer.writerow([full_url_points])

                # if "https" in link_list_item_inner.get("href"):
                #     full_url_points = link_points.get("href")
                #     print(full_url_points)
                #     writer.writerow([full_url_points])
                # else:
                #     # Construct the full URL for links with class "points"
                #     full_url_points = f"{base}{link_points.get('href')}"
                #     print(full_url_points)
                #     writer.writerow([full_url_points])