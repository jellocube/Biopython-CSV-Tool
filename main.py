import importlib
import menus
import config
# import pandas as pd
# import numpy as np

RowRangeStart = 0
RowRangeEnd = 0

# Main Program Starts here
# Main menu selection
menus.printMenuChoices()
menuChoice = menus.inputNumber('Please enter a selection: ')
menus.callMenuChoice(menuChoice)
