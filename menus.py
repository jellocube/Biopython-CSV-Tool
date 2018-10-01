import importlib
import config
import csv
import itertools

filename = config.filename

def printMenuChoices():
    print('\nWhat would you like to do? Selections:')
    print('1. Replace a column')
    print('2. Download abstracts')
    print('3. Download author information')
    print('4. Download publication information')
    print('5. Download title information')
    print('6. DOWNLOAD ALL THE THINGS (all available citation data) \n')
    print('7. Select a new range')
    print('0. Exit\n')

def callMenuChoice(choice):    
    switcher = {
        0: lambda : print('zero'),              # must use lamba or the entire list will execute
        1: lambda :  print('replaceColumn'),
        2: lambda :  print('getAbstracts'),
        3: lambda :  print('getAuthors'),
        4: lambda :  print('getPubs'),
        5: lambda :  print('getTitles'),
        6: lambda :  print('getAll'),
        7: lambda :  selectRange()
    }

    return switcher.get(choice, lambda : print('Invalid selection! Crashing...\n'))()

def inputNumber(message):   # validates user's numerical input
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print('Not an integer! try again.')
            continue
        else:
            return userInput
            break

def inputBinary(message):       # ask for a yes/no response and return 1 or 0
    userInput = str(input(message))
    if userInput[0] == "y" or userInput[0] == "Y":
        return 1
    else:
        return 0


def checkSequence(i, j):    # validates that range row is ordered sequentially
    while j:
        if j < i:
            print('Please enter an end value which precedes start value.')
            j = inputNumber('Please enter a new value: ')
        elif j >= i:
            return j

def getHeaders():           # grabs the headers as an array row
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
    return header_row

def selectRange():         # get user selection
    # Ask for range to be worked on
    RowRangeStart = inputNumber('What row would you like to start at? If this is <1 the script will crash. ')    # Ask for data range
    print('Starting at row ' + str(RowRangeStart))

    RowRangeEnd = inputNumber('What row would you like to end at? ')
    RowRangeEnd = checkSequence(RowRangeStart, RowRangeEnd)
    print('Ending at row ' + str(RowRangeEnd))

    # Open the CSV file and isolate range into array
    with open(filename) as f:
        RowSelection = []       # create table for selection
        reader = csv.reader(itertools.islice(f, RowRangeStart, RowRangeEnd), delimiter=',', quotechar='|') # populate selection with itertools.islice
        for row in reader:
            RowSelection.append(row) # append the rows to RowSelection object

    print('\n...loaded rows ' + str(RowRangeStart) + ' through ' + str(RowRangeEnd) + '\n')

    # Ask to print row titles for redundancy
    if inputBinary('Would you like to read the names of these items? (Highly recommended when committing, for data safety!) '):
        print(getHeaders())     # prints the headers
        for row in RowSelection:
            print(row)
    else:
        print("Just don't screw up the database. \n")

