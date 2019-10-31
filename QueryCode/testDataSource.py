import unittest
from datasource import *

class DataSourceTester(unittest.TestCase):
    def setUp(self):
        user = 'santosb'
        password = 'books347winter'
        self.ds = DataSource()
        self.connection = self.ds.connect()

    def test_number_within_possible_range(self):
        nameOfVariable = 'country'
        variableConditionToMeet = 'US'
        input = self.ds.getCountOfVariableSuccess(self.connection, nameOfVariable, variableConditionToMeet)
        #zero projects and total number of projects
        self.assertGreaterEqual(input,0) and self.assertLessEqual(input, 378661)

    def test_if_parameter_exists_in_table(self):
        nameOfVariable = 'potato'
        variableConditionToMeet = 'US'
        input = self.ds.getCountOfVariableSuccess(self.connection, nameOfVariable, variableConditionToMeet)
        self.assertFalse(input)

    def test_if_condition_exists_in_table(self):
        nameOfVariable = 'country'
        variableConditionToMeet = 'potato'
        input = self.ds.getCountOfVariableSuccess(self.connection, nameOfVariable, variableConditionToMeet)
        self.assertEqual(input == 0)


if __name__ == '__main__':
    unittest.main()