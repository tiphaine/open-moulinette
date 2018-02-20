# -*- coding: utf-8 -*-
"""
Created on Tue Feb  20 14:42:03 2017

@author: tiphaine
"""

import requests
import pandas as pd

from sys import argv


data_url = argv[1]
data_output = argv[2]

print("Downloading data from \"{}\"".format(data_url))
r = requests.get(data_url)

print("Formatting retrieved data")
decoded_r = r.content.decode('utf-8')
data = [line.encode('utf-8').split(';') for line in decoded_r.split('\r\n')]
data_df = pd.DataFrame(data[1:], columns=data[0])

print("Writing data into \"{}\"".format(data_output))
data_df.to_csv(data_output, index=False, sep=';')
