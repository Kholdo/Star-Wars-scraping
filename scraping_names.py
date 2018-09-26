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

#Click Radio button with value 100
cien =driver.find_element_by_xpath("//input[@name='choice' and @value='100']")
cien.click()
print ('click radio button = 100')

#Click Radio button with value 100
generate =driver.find_element_by_xpath("//input[@name='submit' and @value='Generate!']")
generate.click()
print ('click submit button')



#Transfer info to BeautifulSoup
starwars_names_soup=BeautifulSoup(driver.page_source, 'lxml')
print (starwars_names_soup)


div = starwars_names_soup.find_all('td')
print (div)



time.sleep(6)
driver.close()
