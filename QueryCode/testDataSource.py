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
        self.assertEqual(input, 0)

    def test_is_parameter_not_a_number(self):
        nameOfVariable = 2
        variableConditionToMeet = 'US'
        input = self.ds.getCountOfVariableSuccess(self.connection, nameOfVariable, variableConditionToMeet)
        self.assertFalse(input)

    def test_if_condition_is_in_column(self):
        nameOfVariable = 'country'
        variableConditionToMeet = 'Dance'
        input = self.ds.getCountOfVariableSuccess(self.connection, nameOfVariable, variableConditionToMeet)
        self.assertFalse(input)

if __name__ == '__main__':
    unittest.main()