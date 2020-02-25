#------------------------------------------#
# Title: CDInventory.py
# Desc: Script for Assignment 05
# Change Log: (Who, When, What)
# BDunbar, 2020-Feb-23, Created File
#------------------------------------------#

# Declare variables

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # dictionary of data row
lstRow = []  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # Exit the program if the user chooses so
        break
    if strChoice == 'l':
        # Add the functionality of loading existing data
        print('Loading from:')
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': int(lstRow[0]), 'Title': lstRow[1], 'Artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
        print('item in the inventory now: ')
        print('each\'row\':')
        for row in lstTbl:
            print(row)
    elif strChoice == 'a':
        # Add data to the table (2d-list) each time the user wants to add data
        strID = input('Enter an ID: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'id': intID, 'CD Title': strTitle, 'artist': strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            cdRow = ''
            for i in row.values():
                cdRow += str(i) + '|'
            cdRow = cdRow[:-1]
            print(cdRow + '\n')
    elif strChoice == 'd':
        # Add functionality of deleting an entry
        exCD = input('Enter a CD ID to delete from inventory: ')
        rowCounter = 0
        for row in lstTbl:
            if exCD in row.values():
                del lstTbl[rowCounter]
                print('Your CD has been removed from the inventory.\n')
            else:
                print('Your CD does not exist in the inventory.\n')
    elif strChoice == 's':
        # Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'a')
        for row in lstTbl:
            newCD = ''
            for item in row.values():
                newCD += str(item) + ','
            newCD = newCD[:-1] + '\n'
            objFile.write(newCD)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

