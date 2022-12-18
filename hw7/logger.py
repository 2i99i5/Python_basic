from datetime import datetime as dt


def calc_logger(data):
    time = dt.now().strftime('%Y/%m/%d, %H:%M:%S')
    with open('log.csv', 'a') as file:
        file.write('{};{}\n'.format(time, data))