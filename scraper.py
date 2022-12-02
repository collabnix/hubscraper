#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import time
import json
# Selenium 4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.edge.service import Service
# WDM
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# BeautifulSoup
from bs4 import BeautifulSoup

# Change the base_dir with your path.
base_dir = '/Users/ajeetraina/Downloads' + os.sep

# MS Edge Driver
# driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

# Safari Driver


driver = webdriver.Chrome(executable_path = "/Users/ajeetraina/Downloads/chromedriver\ 3")

images = ["store", "official"]
verifiedImages = list()
officialImages = list()

for i in images:
    counter = 1
    while True:
        # Load the HTML page
        driver.get(
            "https://hub.docker.com/search?q=&type=image&image_filter=" + i + "&operating_system=linux&architecture"
                                                                              "=arm64&page=" + str(counter))
        time.sleep(2)
        # Parse processed webpage with BeautifulSoup
        soup = BeautifulSoup(driver.page_source, features="html.parser")
        nextCheck = soup.find('p', attrs={'class': 'styles__limitedText___HDSWL'})
        if not isinstance(nextCheck, type(None)):
            break
        results = soup.find(id="searchResults")
        if isinstance(results, type(None)):
            print("Error: results is NoneType")
            break
        for a in results.find_all('a', href=True):
            print(str(a['href'])[3:])
            if i == "store":
                verifiedImages.append(str(a['href'])[3:])
            else:
                officialImages.append(str(a['href'])[3:])
        counter += 1

    with open(base_dir + 'list_docker_' + i + '_images_RAW.json', 'w', encoding='utf-8') as f:
        if i == "store":
            json.dump(verifiedImages, f, ensure_ascii=False, indent=4)
        else:
            json.dump(officialImages, f, ensure_ascii=False, indent=4)

driver.quit()


