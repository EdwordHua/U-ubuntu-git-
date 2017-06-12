#!/usr/bin/python

import pandas as pd
import numpy as np
import requests

var = pd.Series(range(5))
url = 'http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013743858312764dca7ad6d0754f76aa562e3789478044000'

def getHTMLText(url):
	r = requests.get(url)
	return r.text
	

html = getHTMLText(url)
print(html[:1000])
