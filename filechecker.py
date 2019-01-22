##################################################################################################
#                                                                                                #
#                                                                                                #
#                                                                                                #
#                         Function Definition: Validate Incoming csv file                        #
#                         Author: Batra, Divyesh                                                 #
#  Version: 1.0.0.1                                                                              #
#  Date: 02/14/2018                                                                              #
#                                                                                                #
##################################################################################################


def filechecker(path,filename,list):
    import logging
    import sys
    import os



    LOG_FILENAME = str(path)+'/YourMechanicLog.log'
    logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)
    logging.info('Processing File: ' + filename)
    # check whether incoming file is empty
    if os.stat(filename).st_size == 0:
        logging.info('File' + filename + ' is empty.')
        print('Failed: Check log file for failures at: ' + LOG_FILENAME)
        sys.exit()
    # check whether first line of csv gives an initial number line
    if list[0][0].lower() != 'add':
        logging.info('Unexpected operation: ' + str(list[0][0]) + ' found in first line. The program expects to create an initial interval. Please add initial interval.')
        print('Failed: Check log file for failures at: ' + LOG_FILENAME)
        sys.exit()

    # check whether operation defined is other than add or remove
    for row in range(len(list)):
        if list[row][0].lower() != 'add' and list[row][0].lower() != 'remove':
            logging.info('Unexpected operation: ' + str(list[row][0]) + ' found in line: ' + str(row + 1))
            print('Failed: Check log file for failures at: ' + LOG_FILENAME)
            sys.exit()