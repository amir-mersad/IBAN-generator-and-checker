import requests
import codecs
from bs4 import BeautifulSoup
URL = "https://identinator.com/?for_country=de"
req = requests.get(URL)
decoded_data=req.text.encode().decode('utf-8-sig') 
html = decoded_data
"""  This only finds one of the attributes
number = BeautifulSoup(html, 'html.parser')
final = number.find('input')['name'], ':', soup.find('input')['value']
 This finds all of them  """
soup = BeautifulSoup(html, 'html.parser')
values = [each.attrs['value'] for each in soup.find_all('input')]
iban1 = values[0]
iban2 = values[1]
print(iban1,iban2)

post_url = "https://www.ibancalculator.com/iban_validieren.html"
post_data= {"tx_valIBAN_pi1[iban]":iban1,
            "tx_valIBAN_pi1[fi]":"fi",
            "no_cache":1,
            "Action":"validate IBAN"}
post_req = requests.post(post_url, post_data)
with open('data.txt', "w", encoding="utf-8") as f:
    f.write(post_req.text)
response = post_req.text

""" print(post_req)
print(response)
print(1)
print(1)
print(1) """