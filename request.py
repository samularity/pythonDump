#!/usr/bin/env python3
import sys
import requests

r = requests.get('http://www.der-postillon.com/search/label/Newsticker')
liste_raw = r.text.split('+++') 	
i=0	
liste=[]
for strings in liste_raw:
	if strings[0:2] == '+ ':
		liste.append(strings)
		print(strings)