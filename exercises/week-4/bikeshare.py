#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 11:17:17 2017

@author: smussend
"""

import requests
from pandas.io.json import json_normalize

url1 = "https://gbfs.capitalbikeshare.com/gbfs/en/station_status.json"

url2 = "https://gbfs.capitalbikeshare.com/gbfs/en/station_information.json"


r1= requests.get(url1)

r2 = requests.get(url2)

station_status = r1.json()

info= r2.json()

infodata = info['data']'

info_df = json_normalize(info["data"], "stations")