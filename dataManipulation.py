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


#df = pd.read_csv('data.csv')
'''
class Filterer:
    filters = []

    def __init__(self, data_frame):
        self.data_frame = data_frame

    def __filt(self, where, operator, value):
        if operator == 'EQUALS':
            return (self.data_frame[where] == value)
        elif operator == 'GREATER':
            return (self.data_frame[where] > value)
        elif operator == 'LESS':
            return (self.data_frame[where] < value)
        elif operator == 'GREATER_EQUAL':
            return (self.data_frame[where] >= value)
        elif operator == 'LESS_EQUAL':
            return (self.data_frame[where] <= value)
        elif operator == 'NOT_EQUAL':
            return (self.data_frame[where] != value)
        #return new_data


    def concatinate_filters(self):
        for i in range(len(r.where)):
            self.filters.append(self.__filt(r.where[i], r.operators[i], r.values[i]))
        if len(self.filters) == 1:
            return self.data_frame.loc[(self.filters[0])]
        else:
            if r.logical_operators[i - 1] == 'AND':
                return self.data_frame.loc[np.logical_and.reduce(self.filters)]
            elif r.logical_operators[i - 1] == 'OR':
                return self.data_frame.loc[np.logical_or.reduce(self.filters)]

    def group_by_having(self, data_frame, group_by2, having=None):
        if having:
            if having == 'AVG':
                new_data_frame = data_frame.groupby(group_by2).mean()
            elif having == 'SUM':
                new_data_frame = data_frame.groupby(group_by2).sum()
            elif having == 'COUNT':
                new_data_frame = data_frame.groupby(group_by2).count()
            if r.aggregate_operator != '':
                if r.aggregate_operator == '==':
                    new_data_frame = new_data_frame == r.aggregate_value[0]
                elif r.aggregate_operator == '>':
                    new_data_frame = new_data_frame > r.aggregate_value[0]
                elif r.aggregate_operator == '<':
                    new_data_frame = new_data_frame < r.aggregate_value[0]
                elif r.aggregate_operator == '>=':
                    new_data_frame = new_data_frame >= r.aggregate_value[0]
                elif r.aggregate_operator == '<=':
                    new_data_frame = new_data_frame <= r.aggregate_value[0]
                elif r.aggregate_operator == '!=':
                    new_data_frame = new_data_frame != r.aggregate_value[0]
        else:
            new_data_frame = data_frame.sort_values(group_by2)
        return new_data_frame


    def order_by(self, data_frame, column, ascending):
        if not ascending:
            ordered_data_frame = data_frame.sort_values(column, ascending=False)
        else:
            ordered_data_frame = data_frame.sort_values(column)
        return ordered_data_frame

'''

class Data_minipulator:

    query = ''
    #filters = []

    def is_number(self, str):
        try:
            float(str)
            return True
        except ValueError:
            return False

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
        #print(self.query)
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



