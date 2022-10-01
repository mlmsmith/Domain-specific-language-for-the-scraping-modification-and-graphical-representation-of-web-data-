import unittest
from dataManipulation import DataManipulation
import pandas as pd


class TestDataManipulation(unittest.TestCase):
    """
    Examples of tests used for data manipulation module post integration
    """

    def setUp(self):
        """
        Read in data from testdata.csv and create one instance of DataManipulation to be used by all tests
        :return: instance of DataManipulation
        """
        self.df = pd.read_csv('../../testdata.csv')
        self.dm = DataManipulation()

    def test_many_filters(self):
        """
        Test that the class successfully modifies data data when a large number of filters are applied,
        by comparing the query string generated to be used dataframe.query() method to the excepted one
        :return: query string
        """
        test_categories = ['order_id', 'first_name', 'last_name', 'email', 'Shipping_Address', 'Shipping_Country',
                           'Shipping_Type', 'item', 'Colour', 'size']
        test_operators = ['EQUALS', 'EQUALS', 'EQUALS', 'EQUALS', 'EQUALS', 'EQUALS', 'EQUALS', 'EQUALS', 'EQUALS',
                          'EQUALS']
        test_values = ['1674', 'Baryram', 'Dixcee', 'bdixcee0@infoseek.co.jp', 71, 'Macpherson Plaza', 'China', 5,
                       'Day', 'TShirt', 'Black', 'Small']
        test_logical_operators = ['AND', 'AND', 'OR', 'OR', 'AND', 'OR', 'AND', 'OR', 'AND']

        test_query = "(order_id == 1674) & (first_name == 'Baryram') & (last_name == 'Dixcee') | " \
                     "(email == 'bdixcee0@infoseek.co.jp') | (Shipping_Address == 71) & " \
                     "(Shipping_Country == 'Macpherson Plaza') | (Shipping_Type == 'China') & (item == 5) | " \
                     "(Colour == 'Day') & (size == 'TShirt')"

        self.dm.filter_data(self.df, test_categories, test_operators, test_values,
                            test_logical_operators)

        self.assertEqual(self.dm.query, test_query)

    def test_filter_non_existent_column(self):
        """
        Test that an exception is thrown and caught when a column is attempted to be modified that doesn't exist
        :return: SystemExit(1)
        """
        test_categories = ['Country']  # erroneous column name
        test_operators = ['EQUALS']
        test_values = ['China']

        with self.assertRaises(SystemExit):
            self.dm.filter_data(self.df, test_categories, test_operators, test_values)

    def test_group_by_non_existent_column(self):
        """
        Test that an exception is thrown and caught when a an aggregate function is attempte to be appliad to a column
        that doesn't exist
        :return: SystemExit(1)
        """
        test_group = 'pyjamas'  # erroneous column name

        with self.assertRaises(SystemExit):
            self.dm.group_by_having(self.df, test_group)


if __name__ == 'main':
    unittest.main()
