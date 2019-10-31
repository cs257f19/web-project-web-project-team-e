import unittest
from datasource import *

class DataSourceTester(unittest.TestCase):
    def setUp(self):
        user = 'santosb'
        password = 'books347winter'
        self.ds = DataSource()
        self.connection = self.ds.connect()

    def test_correct_parameters(self):
        nameOfVariable = 'country'
        variableConditionToMeet = 'US'
        self.assertGreater(self.ds.getCountOfVariableSuccess(self.connection, nameOfVariable, variableConditionToMeet),0)


if __name__ == '__main__':
    unittest.main()