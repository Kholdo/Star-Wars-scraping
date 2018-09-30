#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Koldo Pina
Date created: 30/09/2018
Python Version: 3.6
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url_planets = 'http://starwars.wikia.com/wiki/List_of_planets'
url_planets_req = requests.get(url_planets)
planets_html = url_planets_req.text
planets_soup = BeautifulSoup(planets_html, "html.parser")


