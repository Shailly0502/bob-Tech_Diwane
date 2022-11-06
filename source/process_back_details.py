import os
import cv2 as cv
import pandas as pd

def pr(ocr):
    account=[]
    phone=[]
    name=[]
    for i in ocr:
        if('ac' in i.lower() or 'account' in i.lower()):
            for j in i:
                if(j.isdigit()):
                    account.append(j)
        elif('phone' in i.lower()):
            for j in i:
                if(j.isdigit()):
                    phone.append(j)
        elif('name' in i.lower()):
            d=ocr.index(i)
            # if(":" in i.lower()):
            #     d=i.index(':')
            # if("-" in i.lower()):
            #     d=i.index('-')
            # name.append(ocr[d+1:len(i)])
            # print(name)
    y=ocr[d]
    if(":" in y.lower()):
        index=y.index(':')
    if("-" in y.lower()):
        index=y.index('-')
    name.append(y[index+1:len(y)])
    name=(''.join(name))
    name=name.strip()
    account=(''.join(account))
    phone=(''.join(phone))
    return account,phone,name

# x=['Acc. no: - 39880100001236', 'IfSC Code :- BARBOBARRAW', 'Phone no- 9839337748', 'Name :- Anubhav Yadav']
# account,phone,name=pr(x)
# print(account,phone,name)