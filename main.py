import json
import sys

import requests
from bs4 import BeautifulSoup

# url = "https://companies.rbc.ru"

#-------------------------------loading INN from json file--------------------------------------------
try:
    with open("INN.json") as file:
        INN = file.read()

    url = "https://companies.rbc.ru/search/?query=" + INN
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
#------------------------------------------------------------------------------------------------------

# website page loaded
    req = requests.get(url, headers=headers)
    src = req.text

#=========================saving and loading the html version of the site for offline use===========
    # with open("index.html", "w") as file:
    #     src = file.write(src)
    #
    # with open("index.html") as file:
    #     src = file.read()
#===================================================================================================

    soup = BeautifulSoup(src, "lxml")

#------------------------------------search for html elements on a page-----------------------------------
    new_blank = soup.find("a", class_="company-name-highlight").get("href")



    req = requests.get(new_blank, headers=headers)
    src = req.text

    soup = BeautifulSoup(src, "lxml")

    mail = soup.find("div", class_="company-detail__block--tablet-only").find("span", class_="copy-text__icon copy-text-js icon icon__copy").get("data-text")

    print(mail)

# #-------------compiling a dictionary from the target data---------------------

    with open("mailTarget.json", "w") as file:
        json.dump(mail, file, indent=4, ensure_ascii=False)
#-----------------------------------------------------------------------------
except Exception:
    e = sys.exc_info()
    print(e.args)
