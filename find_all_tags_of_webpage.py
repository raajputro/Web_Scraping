import json
from textwrap import indent

import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/'

html_elements = {
    "basic_elements": {
        "html",
        "head",
        "title",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "p",
        "br",
    },
    "formatting_elements": {},
    "forms_and_input_elements": {},
    "frame_elements": {},
    "image_elements": {
        "img",
        "map",
        "area",
        "svg",
        "picture",
        "figure",
        "canvas",
        "figcaption",
    },
    "av_elements": {},
    "link_elements": {
        "a",
        "link",
       # "nav",
    },
    "list_elements": {},
    "table_elements": {},
    "style_elements": {},
    "meta_elements": {},
    "programming_elements": {}
}
#
lst = html_elements['basic_elements']
print(lst if 'h7' in lst else 'missing')

def scrape_page(given_url):
    try:
        response = requests.get(given_url)
        soup = BeautifulSoup(response.text, "html.parser")

        page_title = soup.title.text.split()[0]

        tags = soup.find_all(True)

        for tag in tags:
            # if tag.name in html_elements['basic_elements'] and tag.text.strip():
            #     file_name = f"Basic Elements of Page " + page_title + ".json"
            #     with open(file_name, "w") as jFile:
            #         json.dump([{tag.name: tag.text.strip()}],jFile,indent=4)

            if tag.name in html_elements['link_elements'] and tag.text.strip():
                file_name = f"Link Elements of Page " + page_title + ".json"
                with open(file_name, "a") as jFile: # this will enter only on element, to get all elements, need to create the json data first and them dump
                    json.dump([{tag.text.strip(): tag['href']} if tag.name == 'a' else {tag.name: tag.text.strip()}], jFile, indent=4)



        # with open(f"{page_title}.json", "w") as json_file:
        #     json.dump([{tag.name: tag.text.strip()} for tag in tags if tag.text.strip()], json_file, indent=4)
        #     print(f"{page_title} has been created!")

        # with open(f"{page_title} with all a.json", "w") as jFile:
        #     json.dump([{tag.text.strip(): tag['href']} for tag in tags if tag.name == 'a'], jFile, indent=4)
        #     print("File has been created!")

    except requests.exceptions.RequestException as e:
        print("Failed!",e)

scrape_page(given_url=url)