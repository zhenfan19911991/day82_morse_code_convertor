from bs4 import BeautifulSoup
import requests
import json


response = requests.get("https://www.sckans.edu/~sireland/radio/code.html")

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())

morse_code_all = soup.select("table tr")

morse_code_all[0]

all = {}
for item in morse_code_all[1:]:
    td = item.select('td')
    td_text = []
    for n in td[:2]:
        t = n.text
        t = t.strip('\r\n    ')
        td_text.append(t)
    try:
        all[td_text[0]] = td_text[1]
    except IndexError:
        continue


for key, value in all.items():
    value = value.replace('*', '.')
    all[key] = value

print(all)
# with open('morse_translation.json', 'w') as fp:
#     json.dump(all, fp)
#
# with open('morse_translation.json', 'r') as fp:
#     file_load = json.load(fp)

