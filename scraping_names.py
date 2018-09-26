#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Koldo Pina
Date created: 23/09/2018
Python Version: 3.6
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

driver = webdriver.Firefox()
url = 'http://www.dimfuture.net/starwars/random/generate.php'
driver.get(url)

names = []
for i in range(500):
    #Click Radio button with value 100
    cien =driver.find_element_by_xpath("//input[@name='choice' and @value='100']")
    cien.click()
    print ('click radio button = 100')

    #Click Radio button with value 100
    generate =driver.find_element_by_xpath("//input[@name='submit' and @value='Generate!']")

    generate.click()
    print (f'click submit button {i}')

    #Transfer info to BeautifulSoup
    starwars_names_soup=BeautifulSoup(driver.page_source, 'lxml')
    table = starwars_names_soup.find_all('table')
    rows = table[3].find_all("td")
    for row in rows:
        newname = row.get_text().strip().replace(u'\xa0', u' ')
        if newname not in names:
            names.append([newname])
    print(len(names))
    print ('next')
    # time.sleep(5)
print (len(names))
starwars_names_df = pd.DataFrame(names, columns = ['name'])
driver.close()
