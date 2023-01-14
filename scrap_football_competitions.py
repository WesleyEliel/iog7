import json
from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

driver = webdriver.Chrome()
# implicit wait for 5 seconds
driver.implicitly_wait(5)
# maximize with maximize_window()
driver.maximize_window()
driver.get("https://www.goal.com/fr/toutes-les-competitions")
page_source = driver.page_source
driver.close()
soup = BeautifulSoup(page_source, features="html.parser")
divs = soup.find_all('div', class_='widget-competitions-list-of-all__group')
items = ['Table ', 'Chair ', 'Mirror ', 'Curtain ', 'Almirah ']
file = open('competitions-data.json','w', encoding='utf-8')
items = []
for div in divs:
    for litag in div.findNext('ul').find_all('li'):
        items.append(f'{div.text.strip()} | { litag.a.text.strip()}')
json.dump(items, file, ensure_ascii=False)
file.close()

