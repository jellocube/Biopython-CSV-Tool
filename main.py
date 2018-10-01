import importlib
import menus
import config
import iocheck
import tables
# import pandas as pd
# import numpy as np

# Variables

RowRangeStart = 0
RowRangeEnd = 0

# Main Program Starts here
# Main menu selection

mainLoop = 1

while mainLoop == 1:
    menus.printMenuChoices()
    menuChoice = iocheck.Number('Please enter a selection: ')
    menus.callMenuChoice(menuChoice)
