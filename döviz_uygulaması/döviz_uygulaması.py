import requests
import json
api="http://api.exchangeratesapi.io/v1/latest?access_key=aaf60e2d2d2a174e496f758acf719b8a&format=1"
data=requests.get(api)

data=json.loads(data.text)
day=data["date"]
currency=data["rates"]

print("HOSGELDİNİZ")
try:
    money=input("satmak istediginiz para birimini giriniz:")
    newmoney=input("almak istediginiz para birimini giriniz:")
    para_miktarı=int(input("bozmak istediginiz para miktarı:"))

    newmoney=newmoney.upper()
    money=money.upper()

    x=float(currency[money])
    y=float(currency[newmoney])
    k=y/x

    print("total={}".format(k))
    print("ALACANAGINIZ MİKTAR:{}".format(para_miktarı*k))
except ValueError:
    print("lütfen degerleri dogru giriniz")
