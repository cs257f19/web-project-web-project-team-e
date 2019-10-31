import unittest
<<<<<<< HEAD
from datasource import *

class DataSourceTester(unittest.TestCase):
    def setUp(self):
        user = 'santosb'
        password = 'books347winter'
        self.ds = DataSource(user, password)
        self.connection = self.ds.connect()

    def test_correct_parameters(self):
        nameOfVariable = 'country'
        variableConditionToMeet = 'US'
        self.assertTrue(self.ds.getCountOfVariableSuccess(self.connection, nameOfVariable, variableConditionToMeet))
=======
from datasource import*

class DataSourceTester(unittest.TestCase):
    def setUp(self):

        self.ds = datasource()
    def test_correct_parameters(self):
        user = 'santosb'
        password = 'books347winter'
        self.assertTrue(self.ds.getCountOfVariableSuccess(connection, nameOfVariable, variableConditionToMeet))
>>>>>>> 77fe59ef7dc2fa9e79b1567e7e6cdb3c79176d18


if __name__ == '__main__':
    unittest.main()