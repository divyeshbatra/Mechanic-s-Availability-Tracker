##################################################################################################
#                                                                                                #
#                                                                                                #
#                                                                                                #
#                         Problem Statement: manage disjointed intervals of integers             #
#                         Author: Batra, Divyesh                                                 #
#  Version: 1.0.0.1                                                                              #
#  Date: 02/14/2018                                                                              #
#  Assumptions: The csv file has 3 vales per row: example: "add,3,4". "add 3,4" will not         #
#  work since it misses a comma.                                                                 #
#                                                                                                #
##################################################################################################

import csv
import sys
# import functions created
from disjointoperator import disjointoperator
from filechecker import filechecker
from filewriter import filewriter
from performaddaction import performaddaction
from performremoveaction import performremoveaction
import os


dir_path = os.path.dirname(os.path.abspath(__file__))


filename= str(dir_path) + '/input.csv'

# Read csv file
with open(filename) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    # declare variables/lists
    operation = []  # to store contents of initial file
    pairs = []  # to determine pairs in csv file
    initialList = []  # forumlate initial list
    disjointlist = []  # initial disjoint list
    finaldisjointlist = []  # final disjoint list

    # store contents of csv file in a list
    for row in readCSV:
        operation.append(row)



# validate csv file
filechecker(dir_path,filename,operation)

# determine pairs in csv file
for x in range(len(operation)):
    pairs.append(((operation[x][1]), (operation[x][2])))

# determine initial number line
if operation[0][0].lower() == 'add':
    for item in range((int(pairs[0][0])), int(pairs[0][1]), 1):
        initialList.append((item, item + 1))
        disjointlist = disjointoperator(initialList[:])
    finaldisjointlist.append(disjointlist)


# perform add or remove operation
for i in range(1, len(operation)):
    if operation[i][0].lower() == 'remove':
        initialList = performremoveaction(initialList, int(operation[i][1]), int(operation[i][2]))
        disjointlist = disjointoperator(initialList[:])
        finaldisjointlist.append(disjointlist)

    if operation[i][0].lower() == 'add':
        initialList = performaddaction(initialList, int(operation[i][1]), int(operation[i][2]))
        disjointlist = disjointoperator(initialList[:])
        finaldisjointlist.append(disjointlist)

# perform write operation to write disjoint sets in a text file
filewriter(dir_path,finaldisjointlist)
print('Success: Check Output.txt created at: '+ dir_path+ '/output.txt')








# print(test)
