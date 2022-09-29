'''Modul that find the missing number in one array'''


def get_missing_number(arr):
    '''Function that finds the missing number in array and print it'''
    return [item for item in range(arr [0], arr [-1]+1) if item not in arr]


get_missing_number(arr = [10, 11, 12, 13, 14, 16, 17, 18, 19, 20])
