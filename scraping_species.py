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

species_urls = ['https://en.wikipedia.org/wiki/List_of_Star_Wars_species_(A%E2%80%93E)',
                'https://en.wikipedia.org/wiki/List_of_Star_Wars_species_(F%E2%80%93J)',
                'https://en.wikipedia.org/wiki/List_of_Star_Wars_species_(K%E2%80%93O)',
                'https://en.wikipedia.org/wiki/List_of_Star_Wars_species_(P%E2%80%93T)',
                'https://en.wikipedia.org/wiki/List_of_Star_Wars_species_(U%E2%80%93Z)']
