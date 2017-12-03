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
    """
    btc_eur = "https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=EUR"
    bch_eur = "https://api.coinmarketcap.com/v1/ticker/bitcoin-cash/?convert=EUR"
    iota_eur = "https://api.coinmarketcap.com/v1/ticker/iota/?convert=EUR"

    btc_eur = 0.09889965 * get_info(btc_eur)
    bch_eur = 0.1 * get_info(bch_eur)
    iota_eur = 1 * get_info(iota_eur)

    mymoney = btc_eur + bch_eur
    print("BTC:%.2dEUR\nBCH:%.2fEUR\nIOTA:%.2fEUR\nSum:%.2fEUR " % (btc_eur, bch_eur, iota_eur, mymoney))

def get_info(url):
    "get info and save it"
    try:
        response= requests.get(url, timeout=10.0)
    except requests.exceptions.RequestException as exc:
        print(url + " " + str(exc))
        return
    response = response.text[3:-3].split(',')
    for i in range(len(response)):
        response[i] = response[i].strip().split('"')
        response[i] = list((response[i][1], response[i][3]))
    return(float(response[15][1]))



if __name__ == "__main__":
    main()
