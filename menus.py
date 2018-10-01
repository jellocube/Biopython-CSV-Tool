import importlib
# import config
# import csv
# import itertools
import iocheck
import tables

# filename = config.filename

def printMenuChoices():
    print('\nWhat would you like to do? Selections:')
    print('1. Replace a column')
    print('2. Download abstracts')
    print('3. Download author information')
    print('4. Download publication information')
    print('5. Download title information')
    print('6. DOWNLOAD ALL THE THINGS (all available citation data) \n')
#    print('7. Select a new range')
    print('0. Exit\n')

def callMenuChoice(choice):    
    switcher = {
        0: lambda : exit(),              # must use lamba or the entire list will execute
        1: lambda : tables.replaceColumn(),
        2: lambda : print('getAbstracts'),
        3: lambda : print('getAuthors'),
        4: lambda : print('getPubs'),
        5: lambda : print('getTitles'),
        6: lambda : print('getAll'),
#        7: lambda : tables.selectRange()
    }
    return switcher.get(choice, lambda : print('\nInvalid selection!'))()

