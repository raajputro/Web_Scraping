# # # import requests
# # # from bs4 import BeautifulSoup
# # # import argparse
# # # import json
# # # import csv
# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.options import Options
# # #
# # #
# # # def fetch_html(url, use_selenium=False):
# # #     """Fetch the HTML content of a given URL."""
# # #     try:
# # #         headers = {'User-Agent': 'Mozilla/5.0'}
# # #         if use_selenium:
# # #             options = Options()
# # #             options.add_argument('--headless')
# # #             driver = webdriver.Chrome(options=options)
# # #             driver.get(url)
# # #             html = driver.page_source
# # #             driver.quit()
# # #             return html
# # #         else:
# # #             response = requests.get(url, headers=headers)
# # #             response.raise_for_status()
# # #             return response.text
# # #     except requests.exceptions.RequestException as e:
# # #         print(f"Error fetching {url}: {e}")
# # #         return None
# # #
# # #
# # # def parse_html(html, elements, class_name=None):
# # #     """Parse HTML and extract multiple elements based on tags and optional class."""
# # #     soup = BeautifulSoup(html, 'html.parser')
# # #     results = {}
# # #     for element in elements:
# # #         if class_name:
# # #             results[element] = [el.get_text(strip=True) for el in soup.find_all(element, class_=class_name)]
# # #         else:
# # #             results[element] = [el.get_text(strip=True) for el in soup.find_all(element)]
# # #     return results
# # #
# # #
# # # def save_results(elements, output_file, output_format):
# # #     """Save extracted elements to a file in different formats."""
# # #     if output_format == 'json':
# # #         with open(output_file, 'w', encoding='utf-8') as file:
# # #             json.dump(elements, file, indent=4)
# # #     elif output_format == 'csv':
# # #         with open(output_file, 'w', encoding='utf-8', newline='') as file:
# # #             writer = csv.writer(file)
# # #             for tag, values in elements.items():
# # #                 writer.writerow([tag] + values)
# # #     else:
# # #         with open(output_file, 'w', encoding='utf-8') as file:
# # #             for tag, values in elements.items():
# # #                 file.write(f"{tag} elements:\n")
# # #                 for index, value in enumerate(values, start=1):
# # #                     file.write(f"Element {index}: {value}\n")
# # #                 file.write("\n")
# # #
# # #
# # # def main():
# # #     parser = argparse.ArgumentParser(description="Generic Web Scraper")
# # #     parser.add_argument("url", help="URL of the webpage to scrape")
# # #     parser.add_argument("elements", nargs='+', help="HTML elements to extract (e.g., div p a h1)")
# # #     parser.add_argument("--class_name", help="Optional class name to filter elements", default=None)
# # #     parser.add_argument("--output", help="File to save results", default="output.txt")
# # #     parser.add_argument("--format", help="Output format (text, json, csv)", choices=['text', 'json', 'csv'],
# # #                         default='text')
# # #     parser.add_argument("--selenium", help="Use Selenium for JavaScript-heavy websites", action='store_true')
# # #
# # #     args = parser.parse_args()
# # #
# # #     html = fetch_html(args.url, args.selenium)
# # #     if html:
# # #         elements = parse_html(html, args.elements, args.class_name)
# # #         save_results(elements, args.output, args.format)
# # #         for tag, values in elements.items():
# # #             print(f"{tag} elements:")
# # #             for index, value in enumerate(values, start=1):
# # #                 print(f"Element {index}: {value}")
# # #         print(f"Results saved to {args.output}")
# # #
# # #
# # # if __name__ == "__main__":
# # #     main()
# # ##### Using Selenium ######
# # import requests
# # from bs4 import BeautifulSoup
# # import argparse
# # import json
# # import csv
# # import time
# # from selenium import webdriver
# # from selenium.webdriver.chrome.options import Options
# #
# #
# # def fetch_html(url, use_selenium=False, retries=3, delay=3):
# #     """Fetch the HTML content of a given URL with retries."""
# #     headers = {'User-Agent': 'Mozilla/5.0'}
# #     for attempt in range(retries):
# #         try:
# #             if use_selenium:
# #                 options = Options()
# #                 options.add_argument('--headless')
# #                 driver = webdriver.Chrome(options=options)
# #                 driver.get(url)
# #                 html = driver.page_source
# #                 driver.quit()
# #                 return html
# #             else:
# #                 response = requests.get(url, headers=headers)
# #                 response.raise_for_status()
# #                 return response.text
# #         except requests.exceptions.RequestException as e:
# #             print(f"Attempt {attempt + 1} failed: {e}")
# #             time.sleep(delay)
# #     print(f"Failed to fetch {url} after {retries} attempts.")
# #     return None
# #
# #
# # def parse_html(html):
# #     """Parse HTML and extract all elements with text content."""
# #     soup = BeautifulSoup(html, 'html.parser')
# #     results = {}
# #     for element in soup.find_all():
# #         tag = element.name
# #         text = element.get_text(strip=True)
# #         if text:
# #             results.setdefault(tag, []).append(text)
# #     return results
# #
# #
# # def save_results(elements, output_file, output_format):
# #     """Save extracted elements to a file in different formats."""
# #     if output_format == 'json':
# #         with open(output_file, 'w', encoding='utf-8') as file:
# #             json.dump(elements, file, indent=4)
# #     elif output_format == 'csv':
# #         with open(output_file, 'w', encoding='utf-8', newline='') as file:
# #             writer = csv.writer(file)
# #             for tag, values in elements.items():
# #                 writer.writerow([tag] + values)
# #     else:
# #         with open(output_file, 'w', encoding='utf-8') as file:
# #             for tag, values in elements.items():
# #                 file.write(f"{tag} elements:\n")
# #                 for index, value in enumerate(values, start=1):
# #                     file.write(f"Element {index}: {value}\n")
# #                 file.write("\n")
# #
# #
# # def get_pagination_urls(base_url, max_pages):
# #     """Generate pagination URLs by appending page numbers."""
# #     return [f"{base_url}?page={i}" for i in range(1, max_pages + 1)]
# #
# #
# # def main():
# #     parser = argparse.ArgumentParser(description="Generic Web Scraper")
# #     parser.add_argument("url", help="URL of the webpage to scrape")
# #     parser.add_argument("--output", help="File to save results", default="output.txt")
# #     parser.add_argument("--format", help="Output format (text, json, csv)", choices=['text', 'json', 'csv'],
# #                         default='text')
# #     parser.add_argument("--selenium", help="Use Selenium for JavaScript-heavy websites", action='store_true')
# #     parser.add_argument("--retries", type=int, help="Number of retry attempts for requests", default=3)
# #     parser.add_argument("--delay", type=int, help="Delay between retries in seconds", default=3)
# #     parser.add_argument("--pagination", type=int, help="Number of paginated pages to scrape", default=1)
# #
# #     args = parser.parse_args()
# #
# #     all_results = {}
# #     urls = get_pagination_urls(args.url, args.pagination)
# #
# #     for url in urls:
# #         html = fetch_html(url, args.selenium, args.retries, args.delay)
# #         if html:
# #             elements = parse_html(html)
# #             for tag, values in elements.items():
# #                 all_results.setdefault(tag, []).extend(values)
# #
# #     save_results(all_results, args.output, args.format)
# #     for tag, values in all_results.items():
# #         print(f"{tag} elements:")
# #         for index, value in enumerate(values, start=1):
# #             print(f"Element {index}: {value}")
# #     print(f"Results saved to {args.output}")
# #
# #
# # if __name__ == "__main__":
# #     main()
#
# ######### Using playwright ###########
# import requests
# from bs4 import BeautifulSoup
# import argparse
# import json
# import csv
# import time
# from playwright.sync_api import sync_playwright
#
#
# def fetch_html(url, use_playwright=False, retries=3, delay=3):
#     """Fetch the HTML content of a given URL with retries."""
#     headers = {'User-Agent': 'Mozilla/5.0'}
#     for attempt in range(retries):
#         try:
#             if use_playwright:
#                 with sync_playwright() as p:
#                     browser = p.chromium.launch(headless=True)
#                     page = browser.new_page()
#                     page.goto(url)
#                     html = page.content()
#                     browser.close()
#                     return html
#             else:
#                 response = requests.get(url, headers=headers)
#                 response.raise_for_status()
#                 return response.text
#         except requests.exceptions.RequestException as e:
#             print(f"Attempt {attempt + 1} failed: {e}")
#             time.sleep(delay)
#     print(f"Failed to fetch {url} after {retries} attempts.")
#     return None
#
#
# def parse_html(html):
#     """Parse HTML and extract all elements with text content."""
#     soup = BeautifulSoup(html, 'html.parser')
#     results = {}
#     for element in soup.find_all():
#         tag = element.name
#         text = element.get_text(strip=True)
#         if text:
#             results.setdefault(tag, []).append(text)
#     return results
#
#
# def save_results(elements, output_file, output_format):
#     """Save extracted elements to a file in different formats."""
#     if output_format == 'json':
#         with open(output_file, 'w', encoding='utf-8') as file:
#             json.dump(elements, file, indent=4)
#     elif output_format == 'csv':
#         with open(output_file, 'w', encoding='utf-8', newline='') as file:
#             writer = csv.writer(file)
#             for tag, values in elements.items():
#                 writer.writerow([tag] + values)
#     else:
#         with open(output_file, 'w', encoding='utf-8') as file:
#             for tag, values in elements.items():
#                 file.write(f"{tag} elements:\n")
#                 for index, value in enumerate(values, start=1):
#                     file.write(f"Element {index}: {value}\n")
#                 file.write("\n")
#
#
# def get_pagination_urls(base_url, max_pages):
#     """Generate pagination URLs by appending page numbers."""
#     return [f"{base_url}?page={i}" for i in range(1, max_pages + 1)]
#
#
# def main():
#     #url = "https://www.techlandbd.com/graphics-card"
#     parser = argparse.ArgumentParser(description="Generic Web Scraper")
#     parser.add_argument("url", help="URL of the webpage to scrape")
#     parser.add_argument("--output", help="File to save results", default="output.txt")
#     parser.add_argument("--format", help="Output format (text, json, csv)", choices=['text', 'json', 'csv'],
#                         default='text')
#     parser.add_argument("--playwright", help="Use Playwright for JavaScript-heavy websites", action='store_true')
#     parser.add_argument("--retries", type=int, help="Number of retry attempts for requests", default=3)
#     parser.add_argument("--delay", type=int, help="Delay between retries in seconds", default=3)
#     parser.add_argument("--pagination", type=int, help="Number of paginated pages to scrape", default=1)
#
#     args = parser.parse_args()
#
#     all_results = {}
#     urls = get_pagination_urls(args.url, args.pagination)
#
#     for url in urls:
#         html = fetch_html(url, args.playwright, args.retries, args.delay)
#         if html:
#             elements = parse_html(html)
#             for tag, values in elements.items():
#                 all_results.setdefault(tag, []).extend(values)
#
#     save_results(all_results, args.output, args.format)
#     for tag, values in all_results.items():
#         print(f"{tag} elements:")
#         for index, value in enumerate(values, start=1):
#             print(f"Element {index}: {value}")
#     print(f"Results saved to {args.output}")
#
#
# if __name__ == "__main__":
#     main()
########################### Elements with parent-child-siblings relationship##########
import requests
from bs4 import BeautifulSoup
import argparse
import json
import csv
import time
from playwright.sync_api import sync_playwright


def fetch_html(url, use_playwright=False, retries=3, delay=3):
    """Fetch the HTML content of a given URL with retries."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    for attempt in range(retries):
        try:
            if use_playwright:
                with sync_playwright() as p:
                    browser = p.chromium.launch(headless=True)
                    page = browser.new_page()
                    page.goto(url)
                    html = page.content()
                    browser.close()
                    return html
            else:
                response = requests.get(url, headers=headers)
                response.raise_for_status()
                return response.text
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
    print(f"Failed to fetch {url} after {retries} attempts.")
    return None


# def parse_html(html):
#     """Parse HTML and extract all elements with text content, including parent-child and sibling relationships."""
#     soup = BeautifulSoup(html, 'html.parser')
#     results = []
#
#     def extract_elements(element, parent_path="root", previous_sibling=None):
#         tag = element.name
#         text = element.get_text(strip=True) if element.string else ""
#         path = f"{parent_path} > {tag}" if parent_path else tag
#         sibling_tag = previous_sibling.name if previous_sibling else None
#
#         if text:
#             results.append({"tag": tag, "text": text, "parent": parent_path, "previous_sibling": sibling_tag})
#
#         previous_child = None
#         for child in element.find_all(recursive=False):
#             extract_elements(child, path, previous_child)
#             previous_child = child
#
#     previous_root = None
#     for element in soup.find_all(recursive=False):
#         extract_elements(element, "root", previous_root)
#         previous_root = element
#
#     return results


# def parse_html(html):
#     """Parse HTML and extract all elements with text content, excluding 'style' tags."""
#     soup = BeautifulSoup(html, 'html.parser')
#     results = []
#
#     def extract_elements(element, parent_path="root", previous_sibling=None):
#         tag = element.name
#         # Skip 'style' tags
#         if tag == 'style':
#             return
#
#         text = element.get_text(strip=True) if element.string else ""
#         path = f"{parent_path} > {tag}" if parent_path else tag
#         sibling_tag = previous_sibling.name if previous_sibling else None
#
#         if text:
#             results.append({"tag": tag, "text": text, "parent": parent_path, "previous_sibling": sibling_tag})
#
#         previous_child = None
#         for child in element.find_all(recursive=False):
#             extract_elements(child, path, previous_child)
#             previous_child = child
#
#     previous_root = None
#     for element in soup.find_all(recursive=False):
#         extract_elements(element, "root", previous_root)
#         previous_root = element
#
#     return results

def parse_html(html):
    """Parse HTML and extract all elements with text content, excluding 'style' tags, using relative paths."""
    soup = BeautifulSoup(html, 'html.parser')
    results = []

    def extract_elements(element, parent_path="root", previous_sibling=None):
        tag = element.name
        # Skip 'style' tags
        if tag == 'style':
            return

        text = element.get_text(strip=True) if element.string else ""
        # Use relative path by appending the current tag to the parent's path
        path = f"{parent_path} > {tag}" if parent_path else tag
        sibling_tag = previous_sibling.name if previous_sibling else None

        if text:
            results.append({"tag": tag, "text": text, "parent": parent_path, "relative_path": path,
                            "previous_sibling": sibling_tag})

        previous_child = None
        for child in element.find_all(recursive=False):
            extract_elements(child, path, previous_child)
            previous_child = child

    previous_root = None
    for element in soup.find_all(recursive=False):
        extract_elements(element, "root", previous_root)
        previous_root = element

    return results


def save_results(elements, output_file, output_format):
    """Save extracted elements to a file in different formats."""
    if output_format == 'json':
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(elements, file, indent=4)
    elif output_format == 'csv':
        with open(output_file, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Tag", "Text", "Parent", "Previous Sibling"])
            for element in elements:
                writer.writerow([element["tag"], element["text"], element["parent"], element["previous_sibling"]])
    else:
        with open(output_file, 'w', encoding='utf-8') as file:
            for element in elements:
                file.write(
                    f"Tag: {element['tag']}, Parent: {element['parent']}, Previous Sibling: {element['previous_sibling']}, Text: {element['text']}\n")


def get_pagination_urls(base_url, max_pages):
    """Generate pagination URLs by appending page numbers."""
    return [f"{base_url}?page={i}" for i in range(1, max_pages + 1)]


def main():
    parser = argparse.ArgumentParser(description="Generic Web Scraper")
    parser.add_argument("url", help="URL of the webpage to scrape")
    parser.add_argument("--output", help="File to save results", default="output.json")
    parser.add_argument("--format", help="Output format (text, json, csv)", choices=['text', 'json', 'csv'],
                        default='json')
    parser.add_argument("--playwright", help="Use Playwright for JavaScript-heavy websites", action='store_true')
    parser.add_argument("--retries", type=int, help="Number of retry attempts for requests", default=3)
    parser.add_argument("--delay", type=int, help="Delay between retries in seconds", default=3)
    parser.add_argument("--pagination", type=int, help="Number of paginated pages to scrape", default=1)

    args = parser.parse_args()

    all_results = []
    urls = get_pagination_urls(args.url, args.pagination)

    for url in urls:
        html = fetch_html(url, args.playwright, args.retries, args.delay)
        if html:
            elements = parse_html(html)
            all_results.extend(elements)

    save_results(all_results, args.output, args.format)
    for element in all_results:
        print(
            f"Tag: {element['tag']}, Parent: {element['parent']}, Previous Sibling: {element['previous_sibling']}, Text: {element['text']}")
    print(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
