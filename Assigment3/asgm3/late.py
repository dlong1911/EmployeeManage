
import json

from urllib.request import urlopen

url='https://firebasestorage.googleapis.com/v0/b/funix-way.appspot.com/o/xSeries%2FChung%20chi%20dieu%20kien%2FPYB101x_1.1%2FASM_Resources%2Flate_coming.json?alt=media&token=55246ee9-44fa-4642-aca2-dde101d705de'

thing=urlopen(url,).read()
info=list(json.loads(thing))

def tien_phat(so_ngay):
    for item in info:
        try:
            if int(item['min']) <= so_ngay < int(item['max']):
                tien_phat=so_ngay*int(item['value'])
        except:
            if int(item['min'])<=so_ngay:
                tien_phat=so_ngay*int(item['value'] )
    return tien_phat

