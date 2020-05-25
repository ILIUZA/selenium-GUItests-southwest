import csv
import sys
from GUI.configfiles.log_execution import logTestExecution


def getDataFromFile(file_name):
    """
    :param file_name: a file with data for test case. Usually a file name consists a name of test_function
    :return: data(list) with rows from a file except the first row
    """
    data = []
    log = logTestExecution()
    with open(file_name) as f:
        reader = csv.reader(f, delimiter=';')
        next(f)  # skip the first row
        try:
            for row in reader:
                data.append(row)
        except csv.Error as e:
            log.error('File {}, line {}: {}'.format(file_name, reader.line_num, e))
            sys.exit('File {}, line {}: {}'.format(file_name, reader.line_num, e))
    log.info('Got data <{}> from file <{}>'.format(data, file_name))
    return data
