import unittest
from datasource import*

class DataSourceTester(unittest.TestCase):
    def setUp(self):

        self.ds = datasource()
    def test_correct_parameters(self):
        user = 'santosb'
        password = 'books347winter'
        self.assertTrue(self.ds.getCountOfVariableSuccess(connection, nameOfVariable, variableConditionToMeet))


if __name__ == '__main__':
    unittest.main()
