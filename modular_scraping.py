# # # # # import json
# # # # # import requests
# # # # # from bs4 import BeautifulSoup
# # # # #
# # # # # url = "https://www.scrapethissite.com/pages/"
# # # # #
# # # # # def modularScraping(url):
# # # # #     try:
# # # # #         response = requests.get(url)
# # # # #         soup = BeautifulSoup(response.text, "html.parser")
# # # # #
# # # # #         containers = soup.find(id="pages")
# # # # #
# # # # #         if containers:
# # # # #             elements = containers.find_all(True)
# # # # #             print(elements)
# # # # #             # for element in elements:
# # # # #             #     print(element.name, ":", element.text.strip())
# # # # #             with open("page_data.txt", "a") as file:
# # # # #                 file.write(str(elements))
# # # # #
# # # # #             #print(f"{elem.name} : {elem.text.strip()}" for elem in elements)
# # # # #
# # # # #     except requests.exceptions.RequestException as e:
# # # # #         print("Failed!",e)
# # # # #
# # # # # modularScraping(url)
# # # #
# # # # import requests
# # # # from bs4 import BeautifulSoup
# # # # from lxml import etree
# # # #
# # # # # URL to scrape
# # # # url = "https://www.scrapethissite.com/pages/"
# # # #
# # # # # Send a GET request
# # # # headers = {"User-Agent": "Mozilla/5.0"}
# # # # response = requests.get(url, headers=headers)
# # # #
# # # # if response.status_code == 200:
# # # #     soup = BeautifulSoup(response.text, "html.parser")
# # # #
# # # #     # Convert BeautifulSoup object to lxml etree
# # # #     parser = etree.HTMLParser()
# # # #     tree = etree.fromstring(str(soup), parser)
# # # #
# # # #     # Extract headings and generate XPaths
# # # #     headings = []
# # # #     xpaths = []
# # # #
# # # #     for tag in ["h1", "h2", "h3"]:
# # # #         for index, element in enumerate(tree.xpath(f"//{tag}"), start=1):
# # # #             text = element.text.strip() if element.text else "[Empty Heading]"
# # # #             xpath = tree.getroottree().getpath(element)  # Generate XPath
# # # #             headings.append(text)
# # # #             xpaths.append(xpath)
# # # #
# # # #     # Print extracted headings and their XPaths
# # # #     for i in range(len(headings)):
# # # #         print(f"Heading: {headings[i]}")
# # # #         print(f"XPath: {xpaths[i]}\n")
# # # #
# # # # else:
# # # #     print(f"Failed to retrieve the page. Status code: {response.status_code}")
# # # import requests
# # # from bs4 import BeautifulSoup
# # # from lxml import etree
# # #
# # # # URL to scrape
# # # url = "https://www.scrapethissite.com/pages/"
# # #
# # # # Send a GET request
# # # headers = {"User-Agent": "Mozilla/5.0"}
# # # response = requests.get(url, headers=headers)
# # #
# # # if response.status_code == 200:
# # #     soup = BeautifulSoup(response.text, "html.parser")
# # #
# # #     # Convert BeautifulSoup object to lxml etree
# # #     parser = etree.HTMLParser()
# # #     tree = etree.fromstring(str(soup), parser)
# # #
# # #     # Extract headings and generate relative XPaths
# # #     headings = []
# # #     xpaths = []
# # #
# # #     for tag in ["h1", "h2", "h3"]:
# # #         for element in tree.xpath(f"//{tag}"):
# # #             text = element.text.strip() if element.text else "[Empty Heading]"
# # #
# # #             # Build relative XPath
# # #             parent = element.getparent()
# # #             siblings = parent.findall(tag) if parent is not None else []
# # #             index = siblings.index(element) + 1 if len(siblings) > 1 else None
# # #             relative_xpath = f".//{tag}" if index is None else f".//{tag}[{index}]"
# # #
# # #             headings.append(text)
# # #             xpaths.append(relative_xpath)
# # #
# # #     # Print extracted headings and their relative XPaths
# # #     for i in range(len(headings)):
# # #         print(f"Heading #{i}: {headings[i]}")
# # #         print(f"Relative XPath: {xpaths[i]}\n")
# # #
# # # else:
# # #     print(f"Failed to retrieve the page. Status code: {response.status_code}")
# # import requests
# # from bs4 import BeautifulSoup
# # from lxml import etree
# #
# # # URL to scrape
# # url = "https://www.scrapethissite.com/pages/"
# #
# # # Send a GET request
# # headers = {"User-Agent": "Mozilla/5.0"}
# # response = requests.get(url, headers=headers)
# #
# # if response.status_code == 200:
# #     soup = BeautifulSoup(response.text, "html.parser")
# #
# #     # Convert BeautifulSoup object to lxml etree
# #     parser = etree.HTMLParser()
# #     tree = etree.fromstring(str(soup), parser)
# #
# #     # Extract headings and generate relative XPaths
# #     headings_data = []
# #
# #     for tag in ["h1", "h2", "h3"]:
# #         for element in tree.xpath(f"//{tag}"):
# #             text = element.text.strip() if element.text else "[Empty Heading]"
# #
# #             # Build relative XPath
# #             parent = element.getparent()
# #             siblings = parent.findall(tag) if parent is not None else []
# #             index = siblings.index(element) + 1 if len(siblings) > 1 else None
# #             relative_xpath = f".//{tag}" if index is None else f".//{tag}[{index}]"
# #
# #             headings_data.append((text, relative_xpath))
# #
# #     # Extract links and their relative XPaths
# #     links_data = []
# #     for element in tree.xpath("//a[@href]"):
# #         link_text = element.text.strip() if element.text else "[No Text]"
# #         link_url = element.get("href")
# #
# #         # Build relative XPath for links
# #         parent = element.getparent()
# #         siblings = parent.findall("a") if parent is not None else []
# #         index = siblings.index(element) + 1 if len(siblings) > 1 else None
# #         relative_xpath = f".//a" if index is None else f".//a[{index}]"
# #
# #         links_data.append((link_text, link_url, relative_xpath))
# #
# #     # Print extracted headings and their relative XPaths
# #     print("\nHeadings & XPaths:")
# #     for i, heading, xpath in enumerate(headings_data, start=1):
# #         print(f"Heading{i}: {heading}")
# #         print(f"Relative XPath: {xpath}\n")
# #
# #     # Print extracted links and their relative XPaths
# #     print("\nLinks Found:")
# #     for i, text, url, xpath in enumerate(links_data, start=1):
# #         print(f"Text {i}: {text}")
# #         print(f"URL: {url}")
# #         print(f"Relative XPath: {xpath}\n")
# #
# # else:
# #     print(f"Failed to retrieve the page. Status code: {response.status_code}")
# from importlib.metadata import pass_none
#
# import requests
# from bs4 import BeautifulSoup
# from lxml import etree
# from lxml.html.diff import empty_tags
#
# # URL to scrape
# url = "https://www.scrapethissite.com/pages/"
#
# def tag_data(element_tree, tag) -> []:
#     t_data = []
#     for element in element_tree.xpath(f"//{tag}"):
#         if len(element.text.strip()) > 1:
#             text = element.text.strip()  # .replace("","*")
#             # Build relative XPath
#             parent = element.getparent()
#             siblings = parent.findall(tag) if parent is not None else []
#             index = siblings.index(element) + 1 if len(siblings) > 1 else None
#             if tag == "a[@href]":
#                 link_url = element.get("href")
#                 relative_xpath = f"//a[contains(text(),\"{text}\")]" if index is None else f"//a[{index}]"
#                 t_data.append({"elem_text" : text, "elem_url": link_url, "elem_relative_xpath": relative_xpath})
#             else:
#                 relative_xpath = f"//{tag}" if index is None else f"//{tag}[{index}]"
#                 t_data.append({"elem_text": text, "elem_relative_xpath": relative_xpath})
#     return t_data
#
# # Send a GET request
# headers = {"User-Agent": "Mozilla/5.0"}
# response = requests.get(url, headers=headers)
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#
#     # Convert BeautifulSoup object to lxml etree
#     parser = etree.HTMLParser()
#     tree = etree.fromstring(str(soup), parser)
#
#     # Extract headings and generate relative XPaths
#     headings_data = []
#
#     for tag in ["h1", "h2", "h3"]:
#         headings_data.append(tag_data(tree, tag))
#         # for element in tree.xpath(f"//{tag}"):
#         #     if len(element.text.strip())>1:
#         #         text = element.text.strip()#.replace("","*")
#         #
#         #         # Build relative XPath
#         #         parent = element.getparent()
#         #         siblings = parent.findall(tag) if parent is not None else []
#         #         index = siblings.index(element) + 1 if len(siblings) > 1 else None
#         #         relative_xpath = f"//{tag}" if index is None else f"//{tag}[{index}]"
#         #
#         #         headings_data.append((text, relative_xpath))
#
#     # Extract links and their relative XPaths
#     links_data = tag_data(tree,"a[@href]")
#     # index = 1
#     # for element in tree.xpath("//a[@href]"):
#     #     if len(element.text.strip())>1:
#     #         link_text = element.text.strip()
#     #         link_url = element.get("href")
#     #
#     #         # Build relative XPath for links
#     #         parent = element.getparent()
#     #         siblings = parent.findall("a") if parent is not None else []
#     #         index = siblings.index(element) + 1 if len(siblings) > 1 else None
#     #         relative_xpath = f"//a[contains(text(),\"{link_text}\")]" if index is None else f"//a[{index}]"
#     #
#     #         links_data.append((link_text, link_url, relative_xpath))
#
#     # Print extracted headings and their relative XPaths
#     print("\nHeadings & XPaths:")
#     # for heading, xpath in headings_data:
#     #     print(f"Heading: {heading}")
#     #     print(f"Relative XPath: {xpath}\n")
#     for heading in headings_data:
#         if not heading:
#             pass
#         else:
#             print(f"Heading: {heading}")
#     #print(f"Heading: {heading}" if heading else pass_none() for heading in headings_data)
#
#     # Print extracted links and their relative XPaths
#     print("\nLinks Found:")
#     # for text, url, xpath in links_data:
#     #     print(f"Text: {text}")
#     #     print(f"URL: {url}")
#     #     print(f"Relative XPath: {xpath}\n")
#     for links in links_data:
#         print(f"Links URL: {links['elem_url']}")
#
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")
########################################################################################################################
from importlib.metadata import pass_none

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
                t_data.append({"elem_text" : text, "elem_url": link_url, "elem_relative_xpath": relative_xpath})
            else:
                relative_xpath = f"//{tag}" if index is None else f"//{tag}[{index}]"
                t_data.append({"elem_text": text, "elem_relative_xpath": relative_xpath})
    return t_data

def print_dict_data(dict_list):
    for item in dict_list:
        for key, value in item:
            print(f"{key} : {item}\n")

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

    for tag in ["h1", "h2", "h3"]:
        headings_data.append(tag_data(tree, tag))

    # Print extracted headings and their relative XPaths
    print("\nHeadings & XPaths:")

    # for heading in headings_data:
    #     if heading:
    #         #print(f"Heading: {heading}")
    #print(f"{key}: {value}" if heading else '' for heading in headings_data for key, value in heading)
    print_dict_data(headings_data)


    # Extract links and their relative XPaths
    links_data = tag_data(tree, "a[@href]")

    # Print extracted links and their relative XPaths
    print("\nLinks Found:")

    for links in links_data:
        print(f"Links URL: {links['elem_url']}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")