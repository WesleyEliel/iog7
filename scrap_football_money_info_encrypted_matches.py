import json
import dateutil.parser
from selenium import webdriver
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

driver = webdriver.Chrome()
# implicit wait for 5 seconds
driver.implicitly_wait(5)
# maximize with maximize_window()
driver.maximize_window()
driver.get("https://footballmoney.info/trust.html")
page_source = driver.page_source
driver.close()
soup = BeautifulSoup(page_source, features="html.parser")
tds = soup.select("td:has(> :nth-child(4))")
# items = json.load(open('encrypted-data.json', encoding='utf-8'), )
file = open('encrypted-data.json', 'w', encoding='utf-8')
items = []
print(len(items))
for td in tds[2:]:
    datetag = td.select_one("p:nth-of-type(1) > span")
    date = dateutil.parser.parse(datetag.text.replace('match', '2022'))
    encryptedtag = td.select_one("p:nth-of-type(2)")
    decodertag = td.select_one("p:nth-of-type(4)")
    items.append({
        "date": f'{date.date()}',
        "encrypted_text": f'{encryptedtag.text}',
        "key": f'{decodertag.text}'
    })
print(len(items))
json.dump(items, file, ensure_ascii=False)
file.close()
