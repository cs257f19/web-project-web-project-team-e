import unittest
from datasource import*

class DataSourceTester(unittest.TestCase):
    def setUp(self):
        self.ds = DataSource()

    def test_correct_parameters(self):
        user = 'santosb'
        password = 'books347winter'
        connection = connect(user, password)
        nameOfVariable = 'country'
        variableConditionToMeet = 'US'
        self.assertTrue(self.ds.getCountOfVariableSuccess(connection, nameOfVariable, variableConditionToMeet))


if __name__ == '__main__':
    unittest.main()