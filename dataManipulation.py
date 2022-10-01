import sys

import pandas as pd


class DataManipulation:
    """
    Modifies scraped data stored in data.csv
    """
    query = ''

    def is_number(self, str):
        """
        converts string value into float if the string only contains numerical characters
        :param string: token value
        :return: string if convertable and False boolean if not
        """
        try:
            float(str)
            return True
        except ValueError:
            return False

    def filter_data(self, data_frame, categories, operators, values, logical_operators=None):
        """
        Return new modified data frame containing values that match the description of the applied filters
        :param data_frame: Pandas data frame of data.csv
        :param categories: The column of data that a filter applies to
        :param operators: Numerical operator between categories and value
        :param values: Value that the parameter must fulfil to remain in the data frame
        :param logical_operators: AND or OR to concatenate multiple filters
        :return: New Pandas data frame
        """
        for i in range(len(categories)):
            self.query += '(' + categories[i]
            if operators[i] == 'EQUALS':
                self.query += ' == '
            elif operators[i] == 'GREATER':
                self.query += ' > '
            elif operators[i] == 'LESS':
                self.query += ' < '
            elif operators[i] == 'GREATER_EQUAL':
                self.query += ' >= '
            elif operators[i] == 'LESS_EQUAL':
                self.query += ' <= '
            elif operators[i] == 'NOT_EQUAL':
                self.query += ' != '
            if not self.is_number(values[i]):
                self.query += '\'' + str(values[i]) + '\')'
            else:
                self.query += str(values[i]) + ')'
            if logical_operators:
                if i < len(logical_operators):
                    if logical_operators[int(i)] == 'AND':
                        self.query += ' & '
                    elif logical_operators[int(i)] == 'OR':
                        self.query += ' | '
        try:
            return data_frame.query(self.query)
        except pd.core.computation.ops.UndefinedVariableError as err:
            print(err)
            sys.exit(1)

    def group_by_having(self, data_frame, group, agg_function=None, agg_operator=None, agg_value=None):
        """
        Groups and performs aggregate functions on data
        :param data_frame: Pandas data frame
        :param group: Columns to be grouped by
        :param agg_function: Aggregate function to be applied to column
        :param agg_operator: Numerical operator between column and value
        :param agg_value: Value that the parameter must fulfil to remain in the data frame
        :return:
        """
        if agg_function:
            if agg_function == 'AVG':
                new_data_frame = data_frame.groupby(group).mean()
            elif agg_function == 'SUM':
                new_data_frame = data_frame.groupby(group).sum()
            elif agg_function == 'COUNT':
                new_data_frame = data_frame.groupby(group).count()
            if agg_operator != '':
                if agg_operator == '==':
                    new_data_frame = new_data_frame == agg_value[0]
                elif agg_operator == '>':
                    new_data_frame = new_data_frame > agg_value[0]
                elif agg_operator == '<':
                    new_data_frame = new_data_frame < agg_value[0]
                elif agg_operator == '>=':
                    new_data_frame = new_data_frame >= agg_value[0]
                elif agg_operator == '<=':
                    new_data_frame = new_data_frame <= agg_value[0]
                elif agg_operator == '!=':
                    new_data_frame = new_data_frame != agg_value[0]
        else:
            try:
                new_data_frame = data_frame.sort_values(group)
            except KeyError:
                print('Group_by column does not exist')
                sys.exit(1)
        return new_data_frame

    def order_by(self, data_frame, column, ascending):
        """
        Sort data in either ascending or descending order
        :param data_frame: Pandas data frame
        :param column: The column of data to be sorted
        :param ascending: Boolean for order of sort, True for ascending False for descending
        :return:
        """
        if ascending:
            ordered_data_frame = data_frame.sort_values(column, ascending=True)
        else:
            ordered_data_frame = data_frame.sort_values(column, ascending=False)
        return ordered_data_frame


dm = DataManipulation()


