import requests
import codecs
from bs4 import BeautifulSoup
found_num = 0
counter = 0
while found_num < 2 and counter < 100:
    URL = "https://identinator.com/?for_country=de"
    req = requests.get(URL)
    decoded_data=req.text.encode().decode('utf-8-sig') 
    html = decoded_data
    soup = BeautifulSoup(html, 'html.parser')
    values = [each.attrs['value'] for each in soup.find_all('input')]
    iban1 = values[0]
    iban2 = values[1]
    print(iban1,iban2)
    post_url = "https://www.ibancalculator.com/iban_validieren.html"
    def check(iban):
        post_data= {"tx_valIBAN_pi1[iban]":iban,
            "tx_valIBAN_pi1[fi]":"fi",
            "no_cache":1,
            "Action":"validate IBAN"}
        post_req = requests.post(post_url, post_data)
        response = post_req.text
        global found_num
        correct= "The account number contains a valid checksum"
        correctresponse = "<b>SEPA Credit Transfer is supported.</b></p><p><b>SEPA Direct Debit is supported.</b></p><p><b>B2B is supported.</b></p><p><b>SEPA Instant Credit Transfer is supported."
        if response.find(correct) != -1:
            if response.find(correctresponse) != -1:
                with open('match.txt', "a", encoding="utf-8") as incorrecttxt:
                    incorrecttxt.write(iban1 + "\n")
                print("It is correct (YES)")
                found_num += 1
            else:
                with open('no.txt', "a", encoding="utf-8") as ibantxt:
                    ibantxt.write(iban1 + "\n")
                print("The IBAN didn't have the correct attributes! (NO)")
        else:
            print("incorrect IBAN!")
            with open('incorrect.txt', "a", encoding="utf-8") as notfound:
                notfound.write(iban1 + "\n")
    counter += 1
    check(iban1)
    check(iban2)