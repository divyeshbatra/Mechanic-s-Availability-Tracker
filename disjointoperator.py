##################################################################################################
#                                                                                                #
#                                                                                                #
#                                                                                                #
#                         Function Definition: Create disjointed sets of intervals               #
#                         Author: Batra, Divyesh                                                 #
#  Version: 1.0.0.1                                                                              #
#  Date: 02/14/2018                                                                              #
#                                                                                                #
##################################################################################################


def disjointoperator(disjointlist):
    locallist = disjointlist

# example: if (1,2) (2,3): create (0,0),(1,3)
    i = 0
    while i < (len(locallist) - 1):
        if locallist[i][1] == locallist[i + 1][0]:
            locallist[i + 1] = ((locallist[i][0], locallist[i + 1][1]))
            locallist[i] = ((0, 0))
        i = i + 1

    finallist = []
    #ignore all (0,0) created and push disjointed intervals to a finallist
    for j in range(len(locallist)):
        if locallist[j] != (0, 0):
            finallist.append(locallist[j])

    return (finallist);
