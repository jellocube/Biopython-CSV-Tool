import importlib
import config
import csv
import itertools
import iocheck

filename = config.filename

def getHeaders():           # grabs the headers as an array row
    with open(filename) as f:
        csvArray = csv.reader(f)
        header_row = next(csvArray)
    return header_row

def selectRange():         # get user selection
    # Ask for range to be worked on
    RowRange = [0,0]
    RowRange[0] = iocheck.Number('What row would you like to start at? If this is <1 the script will crash. ')    # Ask for data range
    print('Starting at row ' + str(RowRange[0]))

    RowRange[1] = iocheck.Number('What row would you like to end at? ')
    RowRange[1] = iocheck.Sequence(RowRange[0], RowRange[1])
    print('Ending at row ' + str(RowRange[1]))

    # Open the CSV file and isolate range into array
    with open(filename) as f:
        rowsLoaded = []       # create table for selection
        csvArray = csv.reader(itertools.islice(f, RowRange[0]-1, RowRange[1]), delimiter=',', quotechar='|') # populate selection with itertools.islice
        for row in csvArray:
            rowsLoaded.append(row) # append the rows to rowsLoaded object

    print('\n...loaded rows ' + str(RowRange[0]) + ' through ' + str(RowRange[1]) + '\n')

    # Ask to print row titles for redundancy
    if iocheck.Binary('Would you like to read the names of range ' + str(RowRange) + '? (Highly recommended when committing, for data safety!) '):
        print(getHeaders())     # prints the headers
        print('\n')
        for row in rowsLoaded:
            print(row)
    else:
        print("\nYou have selected a wayward path...")

#   print(RowRange)
    return RowRange

def selectColumn():
    headers = getHeaders()
    for index, column_header in enumerate(headers):
        print(index, column_header)
        
    columnSelected = iocheck.Number('\nPlease select a column number: ')
    print('\nYou have selected: ' + headers[columnSelected] + '\n')
    return columnSelected

def replaceColumn():
    columnSelection = selectColumn()
    RowRange = selectRange()

    newValue = input('\nWhat will the new value of these fields be? ')

    with open(filename) as f:
        csvArray = csv.reader(f)
        csvArraySelected = csv.reader(itertools.islice(f, RowRange[0]-1, RowRange[1]), delimiter=',', quotechar='|') # populate selection with itertools.islice
        print(RowRange)

#        rowCount = 0
#        for row in csvArray:
#            rowCount = rowCount + 1

#        csvArrayBefore = csv.reader(itertools.islice(f, 1, RowRange[0]), delimiter=',', quotechar='|') # populate selection with itertools.islice
#        csvArrayAfter = csv.reader(itertools.islice(f, RowRange[1], rowCount), delimiter=',', quotechar='|') # populate selection with itertools.islice

        print('\nColumns read: ')
        for row in csvArraySelected:
            print(row[columnSelection] + " will be changed to " + newValue)
            row[columnSelection] = newValue
#           print(row[columnSelection] + " is now " + newValue)

            # TODO: append csvArrayBefore + csvArraySelection + csvArrayAfter
            # TODO: save to new CSV file, config.output. Change the input file to config.input
