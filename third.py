import requests
from bs4 import BeautifulSoup

try:
    response = requests.get("https://nonexistent.com")
    soup = BeautifulSoup(response.text,"html.parser")
except requests.exceptions.RequestException as e:
    print("Error occurred while fetching the page", e)