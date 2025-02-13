import requests
from bs4 import BeautifulSoup

url = 'https://www.scrapethissite.com/pages/'

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a",href=True)
    print("Links found in the page:")
    for link in links:
        print(link['href'])

    h1_headings = soup.find_all('h1')
    for h1_heading in h1_headings:
        print(f"Heading is: {h1_heading.text}")

    h3_headings = soup.find_all('h3')
    for i, h3_heading in enumerate(h3_headings,1):
        print(f"#{i} H3_Heading is: {h3_heading.text}")


except requests.exceptions.RequestException as e:
    print("Failed!",e)