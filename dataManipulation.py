import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from reader import r

'''
where = ['Shipping Country', 'order_id']
operators = ['EQUALS', 'GREATER']
values = ['China', 2000]
logical_operator = 'AND'
group_by = 'Shipping Country'
having = 'avg'
'''


class Data_minipulator:

    query = ''

    def is_number(self, str):
        try:
            float(str)
            return True
        except ValueError:
            return False
    '''
      def filter_data(self, data_frame, wheres, operator, value, logical_operator=None):
        for i in range(len(wheres)):
            self.query += '(' + wheres[i]
            if operator[i] == 'EQUALS':
                self.query += ' == '
            elif operator[i] == 'GREATER':
                self.query += ' > '
            elif operator[i] == 'LESS':
                self.query += ' < '
            elif operator[i] == 'GREATER_EQUAL':
                self.query += ' >= '
            elif operator[i] == 'LESS_EQUAL':
                self.query += ' <= '
            elif operator[i] == 'NOT_EQUAL':
                self.query += ' != '
            if not self.is_number(value[i]):
                self.query += '\'' + str(value[i]) + '\')'
            else:
                self.query += str(value[i]) + ')'
            if logical_operator:
                if i < len(logical_operator):
                    if logical_operator[int(i)] == 'AND':
                        self.query += ' & '
                    elif logical_operator[int(i)] == 'OR':
                        self.query += ' | '
        print(self.query)
        return data_frame.query(self.query)
    '''
    def filter_data(self, data_frame, wheres, operator, value, logical_operator=None):
        for i in range(len(wheres)):
            self.query += '(' + wheres[i]
            if operator[i] == 'EQUALS':
                self.query += ' == '
            elif operator[i] == 'GREATER':
                self.query += ' > '
            elif operator[i] == 'LESS':
                self.query += ' < '
            elif operator[i] == 'GREATER_EQUAL':
                self.query += ' >= '
            elif operator[i] == 'LESS_EQUAL':
                self.query += ' <= '
            elif operator[i] == 'NOT_EQUAL':
                self.query += ' != '
            if not self.is_number(value[i]):
                self.query += '\'' + str(value[i]) + '\')'
            else:
                self.query += str(value[i]) + ')'
            if logical_operator:
                if i < len(logical_operator):
                    if logical_operator[int(i)] == 'AND':
                        self.query += ' & '
                    elif logical_operator[int(i)] == 'OR':
                        self.query += ' | '
        print(self.query)
        return data_frame.query(self.query)

    def group_by_having(self, data_frame, group, agg_function=None, agg_operator=None, agg_value=None):
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
            new_data_frame = data_frame.sort_values(group)
        return new_data_frame

    def order_by(self, data_frame, column, ascending):
        if ascending:
            ordered_data_frame = data_frame.sort_values(column, ascending=True)
        else:
            ordered_data_frame = data_frame.sort_values(column, ascending=False)
        return ordered_data_frame


dm = Data_minipulator()

'''
f = Filterer(df)

filtered = f.concatinate_filters()
#print(filtered)
filtered.to_csv('filtered.csv')
aggregated = f.group_by_having(filtered, 'Shipping Country')
#print(aggregated)
aggregated.to_csv('aggregated.csv')
ordered = f.order_by(aggregated, 'Colour', True)
ordered.to_csv('ordered.csv')
#print(ordered)
'''



