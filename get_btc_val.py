#!/usr/bin/env python3
import requests
r = (requests.get("https://www.bitstamp.net/api/v2/ticker/btceur/").text)
r = r[1:-1].split(',')
for i in range(len(r)):
    r[i] = r[i].strip()
    r[i] = r[i].split('"')
    r[i] = list((r[i][1], r[i][3]))
for el in r:
    print (el)
