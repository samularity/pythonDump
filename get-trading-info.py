#!/usr/bin/env python3
"""
This script is used to download btc courses
"""
import os
import time
from time import strftime
import requests


def main():
    """
    main function executes it all
    max 600 requests per 10 minutes
    =>max 60 req per minute
    better save than sorry request only every 2 seconds
    """
    while True:
        get_info()
        time.sleep(2)

def get_info():
    "get info and save it"
    fname = "log.csv"
    url = "https://www.bitstamp.net/api/v2/ticker/btceur/"
    try:
        response= requests.get(url, timeout=10.0)
    except requests.exceptions.RequestException as exc:
        print(url + " " + str(exc))
        return
    response = response.text[1:-1].split(',')
    for i in range(len(response)):
        response[i] = response[i].strip().split('"')
        response[i] = list((response[i][1], response[i][3]))

    print(strftime('%X - ') + str(response[1]) + "EUR")

    if os.path.isfile(fname) is False:
        with open(fname, "w+") as text_file:
            text_file.write("Time;")
            for element in response:
                text_file.write(element[0] + ";")
            text_file.write("\n")
    with open(fname, "a") as text_file:
        text_file.write(strftime('%X;'))
        for element in response:
            text_file.write(element[1] + ";")
        text_file.write("\n")

if __name__ == "__main__":
    main()
