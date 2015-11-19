#!/usr/bin/env python3
import sys

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
print('int:', int(float(sys.argv[1])))
summe = int(float(sys.argv[1])) +int(float(sys.argv[2]))
print (summe)