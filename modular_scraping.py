import json
import requests
from bs4 import BeautifulSoup
from lxml import etree


def tag_data(element_tree, tag) -> []:
    t_data = []
    for element in element_tree.xpath(f"//{tag}"):
        if len(element.text.strip()) > 1:
            text = element.text.strip()
            # Build relative XPath
            parent = element.getparent()
            siblings = parent.findall(tag) if parent is not None else []
            index = siblings.index(element) + 1 if len(siblings) > 1 else None
            if tag == "a[@href]":
                link_url = element.get("href")
                relative_xpath = f"//a[contains(text(),\"{text}\")]" if index is None else f"//a[{index}]"
                t_data.append({"elem_text": text, "elem_url": link_url, "elem_relative_xpath": relative_xpath})
            else:
                relative_xpath = f"//{tag}" if index is None else f"//{tag}[{index}]"
                t_data.append({"elem_text": text, "elem_relative_xpath": relative_xpath})
    return t_data


def print_dict_data(dict_list):
    for items in dict_list:
        if items:
            for item in items:
                for key, value in item.items():
                    print(f"{key} : {value}")
                print("\n")
            print("\n")


# URL to scrape
url = "https://www.scrapethissite.com/pages/"

# Send a GET request
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Convert BeautifulSoup object to lxml etree
    parser = etree.HTMLParser()
    tree = etree.fromstring(str(soup), parser)

    # Extract headings, links and generate relative XPaths
    tag_list = ["h1", "h2", "h3", "a[@href]"]

    headings_data = []
    for tag in tag_list:
        hData = tag_data(tree, tag)
        if hData:
            headings_data.append(hData)

    # Print extracted headings and their relative XPaths
    print("\nHeadings, Links & their XPaths:")
    print_dict_data(headings_data)

    with open("page_data.json", "a") as pJson:
        json.dump(headings_data, pJson,indent=4)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
