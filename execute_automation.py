# # For asynchronous execution
# import asyncio
# from playwright.async_api import async_playwright, Playwright
# # For synchronous execution
from playwright.sync_api import sync_playwright, Playwright

import requests
from bs4 import BeautifulSoup
from pytest_playwright.pytest_playwright import browser

url2 = 'https://www.scrapethissite.com/pages/'
response = requests.get(url2)
soup = BeautifulSoup(response.text, 'html.parser')
all_as = soup.find_all("a")
all_as_5 = all_as[5].get('href')
print("Getting 113th a href: ")
print(all_as_5)
print("Done")

a_elements = soup.select("a")
lst_enu_a_elements = list(enumerate(a_elements))
# for leaelem in lst_enu_a_elements:
#     print(leaelem)
# for i, a_elem in enumerate(a_elements):
#     print(f"a element index: {i}, element text: {a_elem.text}, link: {a_elem.get('href')}")
# for a_elem in a_elements:
#     print(a_elem.get('href'))
one_elem = lst_enu_a_elements[5]
print(one_elem[1])

# For asynchronous execution
# async def run(pw: Playwright):
#     chromium = pw.chromium
#     browser = await chromium.launch()
#     page = await browser.new_page()
#     await page.goto(url2)
#     fElem = next(enumerate(a_elements))
#     await page.locator(fElem).click()
#     await browser.close()
#
# async def main():
#     async with async_playwright() as pw:
#         await run(pw)
#
# asyncio.run(main())
#
def run(play: Playwright):
    chrome = play.chromium
    browser = chrome.launch()
    page = browser.new_page()
    page.goto(url2)
    elem = "//*[contains(@href,'"+all_as_5+"')]"
    page.locator(elem).click()
    page.screenshot(path="clicked.png")
    print("Screenshot captured!")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)