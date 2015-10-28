#!/usr/bin/env python3
import sys
import requests
from time import sleep
while(1):
	sleep(2)
	r = requests.get('http://smarthome.shack/door/open')
	sleep(2)
	r = requests.get('http://smarthome.shack/door/close')
