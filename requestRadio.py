#!/usr/bin/env python3
import sys
import requests
import math

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

r = requests.get('http://www.listenlive.eu/germany.html')
tabelle = find_between(r.text,'<tbody>','</tbody>')
liste_raw = tabelle.split('<tr>') 	
i=0	
liste=[]
for strings in liste_raw:
    #is in format <tr> <td>url</td> <td>stadt</td> <td>icon(dont care)</td>   <td>stream url</td>  <td>gere</td> </tr>
    temp = strings.split('<td>')
    if (len(temp)==6):
        name =  find_between(temp[1],'<b>','</b>' ) 
        url = find_between(temp[4],'"','"')
        gere = temp[5][:temp[5].index( "</t", 0 )]
        spaces1 = ' '* int(math.fabs(30 - len(name)))        
        spaces2 = ' '* int(math.fabs(30 - len(gere)))
        print(name + spaces1 + gere + spaces2 + url)
        #print(url)#stream url