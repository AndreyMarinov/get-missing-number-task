'''Modul that find the missing number in one array'''


def get_missing_number(arr) -> list:
    '''Function that finds the missing number in array and print it

    :param: arr: array that contains the values in it
    :return: list formed from the missing numbers in the array
    '''
    return [item for item in range(arr [0], arr [-1]+1) if item not in arr]
