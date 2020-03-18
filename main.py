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

from PlayerUtil import *


if __name__ == "__main__":
    currentPosition = 1
    initNumber = getHandsInCircle()
    gameArray = shotgun(initNumber)
    while len(gameArray) > 1:
        countAndDisplay(gameArray, currentPosition)
        call(gameArray)



# Main Loop
