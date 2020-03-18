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
    for i in range(0, 2 * len(gameArray) + 1):
        line += " "
    line = line[:positionIndex - 1] + "^" + line[positionIndex + 1:]
    print(line)


def displayHands(gameArray):
    pass
