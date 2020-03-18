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

"""
This file contains all the smaller helper
functions that PlayerUtil uses.
"""


def displayPositionLine(gameArray, ):
    positionLine = "|"
    for i in range(1, len(gameArray) + 1):
        positionLine = positionLine + str(i) + "|"
    print(positionLine)


def displayBreakerLine(gameArray):
    breakerLine = ""
    for i in range(0, 2 * len(gameArray) + 1):
        breakerLine = breakerLine + "-"
    print(breakerLine)


def displayPositionMarker(gameArray, currentPosition):
    positionIndex = (currentPosition * 2)
    line = ""
    for i in range(0, 2 * len(gameArray) + 1):  # this indexing in multiples of 2
        line += " "
    line = line[:positionIndex - 1] + "^" + line[positionIndex + 1:]
    print(line)


def displayHands(gameArray):
    # finding all the hands that are open
    indicesArray = []
    for i in range(0, len(gameArray)):
        if gameArray[i].getIsOpen():
            indicesArray.append(i)
