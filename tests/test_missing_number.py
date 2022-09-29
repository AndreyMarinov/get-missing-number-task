'''Tests for modul that adds missing numbers from the array'''
import unittest

from src.find_the_missing_number import get_missing_number


class TestMissingNumber(unittest.TestCase):
    '''Tests for adding  missing numbers in array'''

    def test_missing_number_in_array(self):
        '''Checks if there is missing number and add it '''
        expected_list = [11, 12, 13, 15, 16, 18]
        result_list = get_missing_number([10, 14, 17, 19, 20])
        self.assertEqual(expected_list, result_list)


    def test_missing_number_in_array_second_test(self):
        '''Checks if there is missing number and add it '''
        expected_list= [11, 12, 13, 14, 15, 17]
        result_list = get_missing_number([10, 16, 18, 19, 20])
        self.assertEqual(expected_list, result_list)


    def test_missing_number_in_array_3rd_test(self):
        '''Checks if there is missing number and add it '''
        expected_list = [11, 12, 13, 14, 16, 17]
        result_list = get_missing_number([10, 15, 18, 19, 20])
        self.assertEqual(expected_list, result_list)


    def test_missing_number_not_in_array(self):
        '''Checks if there is not a number in the array '''
        expected_list = [10, 12, 15, 16, 17, 18]
        result_list = get_missing_number([10, 15, 18, 19, 20])
        assert not expected_list == result_list


if __name__ == '__main__':
    unittest.main()
