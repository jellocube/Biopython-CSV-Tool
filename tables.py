import importlib
import config
import csv
import itertools
import iocheck
import pandas as pd

filename = config.filename

def getHeaders():           # grabs the headers as an array row
    with open(filename) as f:
        csvArray = csv.reader(f)
        header_row = next(csvArray)
    return header_row

def getCSV():
    # Open the CSV file and isolate range into array
    with open(filename) as f:
        rowsLoaded = []       # create table for selection
        csvArray = csv.reader(f) # populate selection with itertools.islice
        for row in csvArray:
            rowsLoaded.append(row) # append the rows to rowsLoaded object
        return rowsLoaded

def getCSVinRowRange(RowRange):
    # Open the CSV file and isolate range into array
    with open(filename) as f:
        rowsLoaded = []       # create table for selection
        csvArray = csv.reader(itertools.islice(f, RowRange[0]-1, RowRange[1]), delimiter=',', quotechar='|') # populate selection with itertools.islice
        for row in csvArray:
            rowsLoaded.append(row) # append the rows to rowsLoaded object
    return rowsLoaded

def getCSVbeforeRange(RowRange):
    # Open the CSV file and isolate range into array
    with open(filename) as f:
        rowsLoaded = []       # create table for selection
        csvArray = csv.reader(itertools.islice(f, 0, RowRange[0]-1), delimiter=',', quotechar='|') # populate selection with itertools.islice
        for row in csvArray:
            rowsLoaded.append(row) # append the rows to rowsLoaded object
    return rowsLoaded

def getCSVafterRange(RowRange):
    # Open the CSV file and isolate range into array
    with open(filename) as f:
        rowsLoaded = []       # create table for selection
        rowsInCSV = getCSV()
        
        rowCount = getCSVrowCount(rowsInCSV)
        csvArray = csv.reader(itertools.islice(f, RowRange[1], rowCount), delimiter=',', quotechar='|') # populate selection with itertools.islice
        for row in csvArray:
            rowsLoaded.append(row) # append the rows to rowsLoaded object
    return rowsLoaded

# def CSVstitcher(beginning, middle, end)
#    

def getCSVrowCount(rowArray):
    rowCount = 0    
    for row in rowArray:
        rowCount = rowCount + 1
    return rowCount

def selectRange():         # get user selection
    RowRange = [0,0]
    RowRange[0] = iocheck.Number('What row would you like to start at? If this is <1 the script will crash. ')    # Ask for data range
    print('Starting at row ' + str(RowRange[0]))
    RowRange[1] = iocheck.Number('What row would you like to end at? ') 
    RowRange[1] = iocheck.Sequence(RowRange[0], RowRange[1])    # checks that RowRange[1] > RowRange[0], otherwise asks for updated value
    print('Ending at row ' + str(RowRange[1]))

    rowsInRange = getCSVinRowRange(RowRange) # Load from the CSV
    print('\n...loaded rows ' + str(RowRange[0]) + ' through ' + str(RowRange[1]) + '\n') # Echo rows loaded

#    if iocheck.Binary('Would you like to read the names of range ' + str(RowRange) + '? (Highly recommended when committing, for data safety!) '):    # Ask to print row titles
#        print(getHeaders())     # prints the headers
#        print('\n')
#        for row in rowsInRange:
#            print(row)      # print the rows in the object of the row range rows
#    else:
#        print("\nYou have selected not to check your work...")

    return RowRange

# Present headers and ask user to select column, which is returned
def selectColumn():
    headers = getHeaders()
    for index, column_header in enumerate(headers):
        print(index, column_header)
        
    columnSelected = iocheck.Number('\nPlease select a column number: ')
    print('\nYou have selected: ' + headers[columnSelected] + '\n')
    return columnSelected

# Menu option to replace all values in a given column for a given range of rows
def replaceColumn():
    columnSelection = selectColumn()
    RowRange = selectRange()


    # get three sets of rows
    rowsBeforeRange = getCSVbeforeRange(RowRange)
    rowsAfterRange = getCSVafterRange(RowRange)
    rowsInRange = getCSVinRowRange(RowRange)
    
    rowCount = getCSVrowCount(rowsInRange)  # TODO: change this so it takes a CSV object input and checks it. Also, add CSV stitcher/splitter definitions and call them here
    newValue = input('\nWhat will the new value of these fields be? ')
    header = ["title", "langcode", "promote", "body", "field_abstract", "field_contributor", "field_coverage", "field_cover_thumbnail", "field_creator", "field_date", "field_format", "field_identifier", "field_language", "field_publisher", "field_related_resources", "field_related_resources_other_", "field_rights", "field_source", "field_subjects", "field_type", "field_url"]

    print('Number of rows, including header: ' + str(rowCount))
    
    print('\nColumns processed: \n')
    with open(filename) as f:
        csvArray = csv.reader(f)

        for row in rowsInRange:
            print('"' + row[columnSelection] + '" will be changed to "' + newValue + '"')
            row[columnSelection] = newValue
            print(row)
            
        print(rowsInRange)

    outputTable = []

    print('\n\n\n\n')

    # combine rows before, in, and after specified range ane export to CSV
    
    for line in rowsBeforeRange:
        print(line)
        outputTable.append(line)

    for line in rowsInRange:
        print(line)
        outputTable.append(line)

    for line in rowsAfterRange:
        print(line)
        outputTable.append(line)
    
    df =  pd.DataFrame(outputTable)
    df.to_csv('output.csv', sep=',', index=False, header = None, escapechar='\\', quoting=csv.QUOTE_NONE)




# try:
# https://stackoverflow.com/questions/34283178/typeerror-a-bytes-like-object-is-required-not-str-in-python-and-csv

#    print(outputTable)
    
#    print(outputTable)
            
#           print(row[columnSelection] + " is now " + newValue)

            # TODO: append csvArrayBefore + csvArraySelection + csvArrayAfter
            # TODO: save to new CSV file, config.output. Change the input file to config.input
