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


class Hand:

    def __init__(self, isOpen, isIn):
        self.open = isOpen
        self.isIn = isIn

    def getIsOpen(self):
        return self.open

    def getIsIn(self):
        return self.isIn


class Player:

    def __init__(self, numberOfHands, handsArray):
        self.numberOfHands = numberOfHands
        self.handsArray = handsArray  # Hands array is a list of hands objects

    def getNumberOfHands(self):
        return self.numberOfHands

    def getHandsArray(self):
        return self.handsArray


def shotgun(numberOfHands):
    # Shotgun creates the game array and counts out the number of hands
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


def countAndDisplay(gameArray):
    counter = 0
    for i in range(0, len(gameArray)):
        if gameArray[i].getIsOpen():
            counter += 1
    numberOpen = counter * 5
    print("The number in the circle is " + str(numberOpen))
    return numberOpen


'''
def displayGame(gameArray, currentPosition):
    displayPositionLine(gameArray)
    displayPositionMarker(gameArray, currentPosition)
    displayBreakerLine(gameArray)
    displayHands(gameArray)
    
'''
