import os
import time
import json
import csv
import re
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


csv_file = open('results.csv', 'w')

# create the csv writer
writer = csv.writer(csv_file)

writer.writerow(['Image Name','Downloads','Stars'])




driver = webdriver.Chrome(executable_path = "/Users/ajeetraina/Downloads/chromedriver\ 3")

images = ["official"]
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

        imagesList = results.find_all('a',attrs={'data-testid': 'imageSearchResult'})
        
        if len(imagesList) == 0:
            break

        for image in imagesList:

            # Getting the Name of the Image
            image_name = image.find('span',{"class":re.compile('.*MuiTypography-root.*')}).text

            counts = image.find_all('p',{"class":re.compile('.*MuiTypography-root MuiTypography-body1.*')})

            #Download Counts
            if len(counts) <=  1:
                download_count = "0"
                stars_count = counts[0].text
            
            else:
                download_count = counts[0].text

                # Starts Count
                stars_count = counts[1].text

            #print(image.find_all('div',{"class" : regex}))
            
            writer.writerow([image_name,download_count,stars_count])
            

        if len(imagesList) == 0:
            break
        counter += 1
        


    with open(base_dir + 'list_docker_' + i + '_images_RAW.json', 'w', encoding='utf-8') as f:
        if i == "store":
            json.dump(verifiedImages, f, ensure_ascii=False, indent=4)
        else:
            json.dump(officialImages, f, ensure_ascii=False, indent=4)

            
csv_file.close()
driver.quit()
