##################################################################################################
#                                                                                                #
#                                                                                                #
#                                                                                                #
#                         Function Definition: Perform remove operation on intervals             #
#                         Author: Batra, Divyesh                                                 #
#  Version: 1.0.0.1                                                                              #
#  Date: 02/14/2018                                                                              #
#                                                                                                #
##################################################################################################


def performremoveaction(firstlist,pairInitial, pairLast):
    removelist=[]

    # perform remove operation
    for i in range(pairInitial,pairLast,1):
        removelist.append((i, i + 1))
    for item in removelist:
        while firstlist.count(item)>0:
            firstlist.remove(item)

    return(firstlist);
