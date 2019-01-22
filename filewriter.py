##################################################################################################
#                                                                                                #
#                                                                                                #
#                                                                                                #
#                         Function Definition: Write results to an output file                   #
#                         Author: Batra, Divyesh                                                 #
#  Version: 1.0.0.1                                                                              #
#  Date: 02/14/2018                                                                              #
#                                                                                                #
##################################################################################################


def filewriter(path,finallist):

    file=open(str(path) + '/output.txt','w')
    startbracket='['
    endbracket=']'
    localfinallist=finallist
    for i in range(len(localfinallist)):
        file.write(startbracket + str(list(localfinallist[i])) + endbracket+ '\n')
    file.close();