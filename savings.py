#!/usr/bin/python3.4

from decimal import *
from datetime import datetime

startingSavingAmount = Decimal('0.00')
incrementAmount = Decimal('0.00')
totalAmount = Decimal('0.00') 


def __init__():
    getcontext().prec = 2
    global startingSavingAmount 
    startingSavingAmount = Decimal('0.01')
    global incrementAmount
    incrementAmount = Decimal('0.01')
    amountToSaveToday()

def amountToSaveToday():
    day = datetime.now().timetuple().tm_yday
    global startingSavingAmount
    global totalAmount
    startamount = startingSavingAmount 
    x = 0
    fmt = '{0:<6} {1:<6}'
    print(fmt.format('save', 'total'))
    print(fmt.format('-' * 6, '-' * 6))
    for x in range(0, 365):
        totalAmount = Decimal(totalAmount) + Decimal(startamount)
        print(fmt.format(startamount, totalAmount))
        startamount = Decimal(startamount) + Decimal(incrementAmount)
        x + 1
    print('This is the amount to save today - ' + str(totalAmount))

if __name__ == "__main__":
    __init__()
