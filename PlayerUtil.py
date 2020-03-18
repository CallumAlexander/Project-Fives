#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# -*- This file is Property of Callum 'Cal' Alexander -*-
# -*- CONTACT INFORMATION -*-
# -*- Email : s1931801@ed.ac.uk -*-
# -*- Instagram : cal.zander -*-
# -*- Twitter : calzander -*-

"""
Created on Tue Mar 17 19:25:14 2020
@author: cal
"""

'''
PlayerUtil contains the higher level functions and classes 
that main.py uses.
'''

from time import sleep
from misc import *


class Hand:

    def __init__(self, isOpen, isIn):
        self.open = isOpen
        self.isIn = isIn


class Player:

    def __init__(self, numberOfHands, handsArray):
        self.numberOfHands = numberOfHands
        self.handsArray = handsArray  # Hands array is a list of hands objects


def shotgun(numberOfHands):
    gameArray = []
    for i in range(0, numberOfHands):
        tempHand = Hand(False, True)
        gameArray.append(tempHand)

    print("SHOTGUN !!")
    sleep(1.5)
    print("From my right to my right...")
    sleep(1.5)
    for i in range(1, numberOfHands + 1):
        print(str(i * 5))
        sleep(0.8)

    return gameArray


def getHandsInCircle():
    number = int(input("Input the number of hands > "))
    while number < 2:
        print("You don't have enough hands in the ring !")
        print("Try again")
        number = int(input("Input the number of hands > "))

    return number


def displayHands(gameArray, currentPosition):
    displayPositionLine(gameArray)
    displayPositionMarker(gameArray, currentPosition)
    displayBreakerLine(gameArray)
