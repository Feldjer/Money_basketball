from bs4 import BeautifulSoup

import urllib.request

# Bypassing dynamic site protection

def dynamic_link_search():
    startOfLink = '//*[@id="'
    endOfLink = ']'
    page = BeautifulSoup(open('html_code_dinamical_number.txt', encoding='utf-8'), 'html.parser')  # Saving an html page
    for i in page.find_all("div", class_='input__wrapper c-registration__field--number'):
        string = str(i)
        break
    position = string.find('auth_phone_number_')
    string = string[position:]
    position = string.find(' placeholder')
    dynamicLink = startOfLink + string[:position] + endOfLink
    return dynamicLink
