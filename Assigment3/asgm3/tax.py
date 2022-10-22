

import xml.etree.ElementTree as ET 
from urllib.request import urlopen


url='https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Ftax.xml?alt=media&token=f7a6f73d-9e6d-4807-bb14-efc6875442c7'
html=urlopen(url,).read()

thing=ET.fromstring(html)

lst=list()
tax=list()
lst=thing.findall('tax')
idx=0
for item in lst:
    tax.append({})
    tax[idx]['min']=item.find('min').text
    if (item.find('max') is not None):
        tax[idx]['max']=item.find('max').text
    tax[idx]['value']=item.find('value').text
    idx+=1

def tinh_thue(luong):
    for item in tax:
        try:
            if int(item['min']) <= luong < int(item['max']):
                muc_thue=int(item['value'])
        except:
            if int(item['min'])<=luong:
                muc_thue=int(item['value'] )
    return muc_thue       

