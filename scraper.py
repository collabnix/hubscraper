# Base Libraries 
import os
import time
import csv
import re

# Selenium 4 for loading the Browser Driver 
from selenium import webdriver

# BeautifulSoup Library used for Parsing the HTML 
from bs4 import BeautifulSoup

# Change the base_dir with your path.
base_dir = '/Users/ajeetraina/Downloads' + os.sep

# Opening the CSV File Handle
csv_file = open('results.csv', 'w')

# Create the csv writer
writer = csv.writer(csv_file)

# Writing the Headers for the CSV File
writer.writerow(['Image Name','Downloads','Stars'])


# Initialising the Chrome Driver
driver = webdriver.Chrome(executable_path = "/Users/ajeetraina/Downloads/chromedriver\ 3")

# Images Type which have to filitered from the DockerHub 
images = ["official"]
verifiedImages = list()
officialImages = list()

for i in images:
    counter = 1
    while True:
    
        # Load the Docker Hub HTML page
        driver.get(
            "https://hub.docker.com/search?q=&type=image&image_filter=" + i + "&operating_system=linux&architecture"
                                                                              "=arm64&page=" + str(counter))
        
        # Delay to load the contents of the 
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
            break   # Stopping the parsing when no images are found

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

                # Stars Count
                stars_count = counts[1].text
            
            # Writing the Image Name, Download Count and Stars Count to File
            writer.writerow([image_name,download_count,stars_count])
            

        if len(imagesList) == 0:
            break
        
        counter += 1

# Closing of the CSV File Handle           
csv_file.close()

# Closing of the Chrome Driver 
driver.quit()
