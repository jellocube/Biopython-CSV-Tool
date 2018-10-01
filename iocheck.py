def Number(message):   # validates user's numerical input
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print('Not an integer! try again.')
            continue
        else:
            return userInput
            break

def Binary(message):       # ask for a yes/no response and return 1 or 0
    userInput = str(input(message))
    if userInput[0] == "y" or userInput[0] == "Y":
        return 1
    else:
        return 0

def Sequence(i, j):    # validates that range row is ordered sequentially
    while j:
        if j < i:
            print('Please enter an end value which precedes start value.')
            j = Number('Please enter a new value: ')
        elif j >= i:
            return j
