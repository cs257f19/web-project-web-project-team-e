import unittest
from datasource import *

class DataSourceTester(unittest.TestCase):
    def setUp(self):
        user = 'loye'
        password = 'tablet984spring'
        self.ds = DataSource()
        self.connection = self.ds.connect()

    def test_correct_parameters(self):
        nameOfVariable = 'country'
        variableConditionToMeet = 'US'
        self.assertGreaterEqual(self.ds.getCountOfVariableSuccess(self.connection, nameOfVariable, variableConditionToMeet),0)


if __name__ == '__main__':
    unittest.main()