import json
import requests
from bs4 import BeautifulSoup

parent_url = 'https://www.scrapethissite.com'
url = 'https://www.scrapethissite.com/pages/'

def scrape_page(given_url):
    try:
        response = requests.get(given_url)
        soup = BeautifulSoup(response.text, "html.parser")

        tags = soup.find_all(True)

        page_title = soup.find('title').text
        file_name =page_title.split('|')[0] +".json"
        with open(file_name, "w") as json_file:
            json.dump([{tag.name: tag.text.strip()} for tag in tags], json_file)

    except requests.exceptions.RequestException as e:
        print("Failed!",e)

def find_sub_pages(given_url):
    try:
        response = requests.get(given_url)
        soup = BeautifulSoup(response.text, "html.parser")

        links = soup.find_all("a",href=True)
        print("Links found in the page:")
        for link in links:
            print(link['href'])
        return links

    except requests.exceptions.RequestException as e:
        print("Failed!",e)

links = find_sub_pages(url)

for link in links:
    print(parent_url+link['href'])
    scrape_page(parent_url+link['href'])