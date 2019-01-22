##################################################################################################
#                                                                                                #
#                                                                                                #
#                                                                                                #
#                         Function Definition: Perform add operation on intervals                #
#                         Author: Batra, Divyesh                                                 #
#  Version: 1.0.0.1                                                                              #
#  Date: 02/14/2018                                                                              #
#                                                                                                #
##################################################################################################


def performaddaction(firstlist,pairInitial, pairLast):
    addlist=[]
    #change list to set
    #incoming list from last operation
    firstlistset=set(firstlist)

    # example add (2,5): (2,3),(3,4),(4,5) based on pairs received
    for i in range(pairInitial,pairLast,1):
        addlist.append((i, i + 1))
    #change list to set
    addlistset=set(addlist)
    #perform union of two sets
    finalset=firstlistset.union(addlistset)
    #sort the results
    finallist=list(sorted(finalset))
    return(finallist);