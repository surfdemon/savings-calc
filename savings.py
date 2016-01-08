#!/usr/bin/python3.4
from decimal import *
from datetime import datetime


startingSavingAmount = Decimal('0.00')
incrementAmount = Decimal('0.00')
totalAmount = Decimal('0.00') 


def __init__():
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
    for x in range(0, day):
        totalAmount = Decimal(totalAmount) + Decimal(startamount)
        startamount = Decimal(startamount) + Decimal(incrementAmount)
        x + 1
    print('Today save: £' + str(Decimal(startamount) - Decimal('0.01') ) + ' You should now have a total of: £' + str(totalAmount))


if __name__ == "__main__":
    __init__()
