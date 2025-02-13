import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/'

def scrape_page(given_url):
    try:
        response = requests.get(given_url)
        soup = BeautifulSoup(response.text, "html.parser")

        tags = soup.find_all(True)
        # print("All tags found in the page:")
        # for tag in tags:
        #     print(tag.name)

        # with open("tags.txt", "w") as f:
        #     for tag in tags:
        #         f.write(f"{tag.name}\n")
        #         print("Tags and values written to tags.txt file")
        page_title = soup.title.string()
        with open(f"{page_title}.json", "w") as json_file:
            json.dump([{tag.name: tag.text.strip()} for tag in tags], json_file)

    except requests.exceptions.RequestException as e:
        print("Failed!",e)