import requests
from bs4 import BeautifulSoup
from lxml import etree

# URL to scrape
url = "https://www.scrapethissite.com/pages/"


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
    #print(f"Sent Dict List: {dict_list}")
    for items in dict_list:
        if items:
            for item in items:
                for key, value in item.items():
                    print(f"{key} : {value}")
                print("\n")
            print("\n")


# Send a GET request
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Convert BeautifulSoup object to lxml etree
    parser = etree.HTMLParser()
    tree = etree.fromstring(str(soup), parser)

    # Extract headings and generate relative XPaths
    headings_data = []

    for tag in ["h1", "h2", "h3", "a[@href]"]:
        hData = tag_data(tree, tag)
        if hData:
            headings_data.append(hData)

    # Print extracted headings and their relative XPaths
    print("\nHeadings & XPaths:")
    print_dict_data(headings_data)

    # for heading in headings_data:
    #     #print(f"Heading: {heading}\n")
    #     if heading:
    #         for item in heading:
    #             for key, value in item.items():
    #                 print(f"{key} : {value}")
    #             print("\n")
    #         print("\n")

    # # Extract links and their relative XPaths
    # links_data = tag_data(tree, "a[@href]")
    #
    # # Print extracted links and their relative XPaths
    # print("\n\n\nLinks Found:")
    #
    # for links in links_data:
    #     print(f"Links: {links}")
    #     print(f"Links URL: {links['elem_url']}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
