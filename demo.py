# pip install requests beautifulsoup4
# pip install pytest-playwright
# playwright install

import requests

from bs4 import BeautifulSoup
import time

url = 'https://dev-meetingspace.askmak.ai'
url2 = 'https://www.sailor.clothing/category/men'

# html_doc = """
#         <html>
#             <head>
#                 <title> Sample Page </title>
#             </head>
#             <body>
#                 <h1>H1-1</h1>
#                 <h1>H1-2</h1>
#                 <h2>H2</h2>
#                 <p class="content">This is a paragraph content.</p>
#                 <a href="https://example.com">Go for more Examples</a>
#             </body>
#         </html>
# """
# soup = BeautifulSoup(html_doc, 'html.parser')
#
# #elements = soup.find_all('a')
# elements = soup.select("a")
# for elem in elements:
#     print(f"Links: {elem['href']}")
# #
# # for elm in elements:
# #     print(elm)
# #     #print(elm.text)


response = requests.get(url2)
print(response)
#time.sleep(10)
soup = BeautifulSoup(response.text, 'html.parser')
a_elements = soup.select("a")
for i, a_elem in enumerate(a_elements):
    print(f"a element index: {i}, element text: {a_elem.text}, link: {a_elem.get('href')}")