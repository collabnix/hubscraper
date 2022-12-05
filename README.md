# python-dockerhub-scraper
A Docker image that scraps Docker Hub official and verfied Images.

A Handy Python script for web scraping dynamically the Docker Hub website. 
This script is capable of fetching a list of Docker Extensions from the Docker Hub


## Getting Started

## Pre-requisite

- Install Python 3.9+
- Download [Chrome Driver](https://chromedriver.storage.googleapis.com/index.html?path=108.0.5359.71/)


## Buiding it locally

### Clone the repository

```
git clone https://github.com/collabnix/hubscraper/
```

### Install the required modules

```
pip3 install -r requirements.txt
```

### Modify the script

Go to Line 17 and make the necessary changes:

```
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
```



### Execute the script

```
python3 scraper.py
```



<img width="784" alt="image" src="https://user-images.githubusercontent.com/34368930/205429792-03e64b91-72f0-4e9a-83d9-e0c34b850be4.png">


## Building with Docker


```
git clone https://github.com/collabnix/hubscraper/
docker build -t ajeetraina/hubscraper .
```

## Running the Hubscraper in a Docker container

```
docker run --platform=linux/amd64 -it -w /app -v $(pwd):/app ajeetraina/scraperhubb bash
root@960e8b9fa2c2:/usr/workspace# python scraper.py 
[WDM] - Downloading: 100%|███████████████████████████████████████████████████████████████| 6.96M/6.96M [00:00<00:00, 8.90MB/s]
```



