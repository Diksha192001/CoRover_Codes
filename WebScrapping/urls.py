import requests
from bs4 import BeautifulSoup
import csv
# from urllib.parse import urljoin
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

# opt = Options()
# opt.add_experimental_option("detach", True)
# serv_obj = Service("C:\chromedriver\chromedriver.exe")
# driver = webdriver.Chrome(service=serv_obj, options=opt)
# driver.get("https://www.sebi.gov.in/")
# driver.find_element(By.XPATH,"//a[@id='menu1']").click()
# get_url = driver.current_url
# print(get_url)


urls = [
        "https://www.sebi.gov.in/",
        "https://www.sebi.gov.in/about.html",
        "https://www.sebi.gov.in/legal.html",
        "https://www.sebi.gov.in/enforcement.html",
        "https://www.sebi.gov.in/filings.html",
        "https://www.sebi.gov.in/reports-and-statistics.html",
        "https://www.sebi.gov.in/status.html",
        "https://www.sebi.gov.in/media-and-notifications.html" ]


for url in urls:

    with open('C:\\Users\\DIKSHA\\Documents\\sebi.csv', 'a', newline='\n') as f:
        # f.write(url) 
        writer = csv.writer(f)
        writer.writerow([url])


    page = requests.get(url)

    soup = BeautifulSoup(page.content, "html.parser")
    base = "https://www.sebi.gov.in/"

    # links = soup.find_all("a",class_="sf-with-ul")  --- this was commented
    links = soup.find_all("a", class_="list_item_inner")

    for link in links:
        if "https" in link.get("href"):
            site = link.get("href")
            print(site)

            with open('C:\\Users\\DIKSHA\\Documents\\sebi.csv', 'a', newline='\n') as f:
                # f.write(site)
                writer = csv.writer(f)
                writer.writerow([site])


        else:
            site = base+link.get("href")
            print(site)

            with open('C:\\Users\\DIKSHA\\Documents\\sebi.csv', 'a', newline='\n') as f:
                # f.write(site)
                writer = csv.writer(f)
                writer.writerow([site])


    




















# for link in links:
#     print(link.get("href"))

# form_element = soup.find("form")

# if form_element:
#     # Find the div element inside nav
#     div_element = form_element.find("div", class_=["full_width_menu", "wrapper clearfix", "wsmenucontainer clearfix"])

#     if div_element:
#         # Find all div head elements inside div
#         div_elementt = div_element.find_all("div", class_="header")

#         if div_elementt:
#             # Find all nav head elements inside div
#             nav_element = div_elementt.find_all("nav", class_="wsmenu clearfix")

#             if nav_element:
#                 # Find all ul head elements inside div
#                 ul_element = nav_element.find_all("ul", class_="mobile-sub wsmenu-list sf-menu sf-js-enabled sf-arrows")

#                 if ul_element:
#                     # Find all li elements inside ul
#                     li_elements = ul_element.find_all("li")
#                     print(li_elements)

                    # for li_element in li_elements:
                    #     # Extract text content from each li element
                    #     item_text = li_element.get_text(strip=True)
                    #     print(item_text)

#     # class="sf-with-ul"

# tab_elements = links.select('.sf-with-ul')  # Replace '.your-tab-selector' with the actual CSS selector for your tabs

# tabs = {}
# for tab_element in tab_elements:
#     tab_name = tab_element.text.strip()
#     tab_url = urljoin("https://www.sebi.gov.in/", tab_element['href'])
#     tabs[tab_name] = tab_url

# print(tabs)
