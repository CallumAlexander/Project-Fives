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

from random import randint as rnd
from time import sleep


class Hand:

    def __init__(self, isOpen, isIn):
        self.open = isOpen
        self.isIn = isIn

    def getIsOpen(self):
        return self.open

    def getIsIn(self):
        return self.isIn

    def setIsOpen(self, newVal):
        # TODO - implement exceptions for bool
        self.open = newVal

    def setIsIn(self, newVal):
        # TODO - implement exceptions for bool
        self.isIn = newVal

    def AIchooseCall(self):
        handCall = rnd(0, 1)
        if handCall == 0:
            self.setIsOpen(False)
        else:
            self.setIsOpen(True)


# End of Class
# ------------------------------------


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


def display(gameArray, currentPosition):
    numberOpen = count(gameArray)
    playerHand = ""
    if gameArray[0].getIsOpen():
        playerHand = "open"
    else:
        playerHand = "closed"

    print("\nYou are " + playerHand)
    print("The number in the circle is " + str(numberOpen) + "\t" + " It's hand " + str(currentPosition) + "'s turn")
    return numberOpen


# TODO - Implement the full displayGame function by finishing the displayHands function
'''
def displayGame(gameArray, currentPosition):
    displayPositionLine(gameArray)
    displayPositionMarker(gameArray, currentPosition)
    displayBreakerLine(gameArray)
    displayHands(gameArray)
'''


def callHand(gameArray):
    # Setting your call
    playerCall = input("Your call for the turn (Open or Closed) > ")
    if playerCall == "Open":
        gameArray[0].setIsOpen(True)
    else:
        gameArray[0].setIsOpen(False)

    # Setting the AI calls
    for i in range(1, len(gameArray)):
        gameArray[i].AIchooseCall()

    return gameArray


def callNumber(gameArray, currentPosition):
    playerIndex = 0
    if currentPosition == playerIndex:
        # TODO - validate player number call to only accept numbers of 5
        playerNumberCall = input("Your number call for this turn")
        numberOpen = count(gameArray)


def count(gameArray):
    counter = 0
    for i in range(0, len(gameArray)):
        if gameArray[i].getIsOpen():
            counter += 1

    numberOpen = counter * 5
    return numberOpen
