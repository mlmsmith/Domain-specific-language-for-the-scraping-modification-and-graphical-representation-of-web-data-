import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pylab as pl

'''
class DataVisualisation:

    def __init__(self, data_frame, plot_type, x_axis, y_axis):
        self.data_frame = data_frame
        if plot_type == 'BAR_PLOT':
            self.plot_type = 'bar'
        else:
            self.plot_type = 'plot'
        self.x_axis = x_axis
        self.y_axis = y_axis

    def construct_plot(self):
        for column in range(len(self.x_axis)):
            eval('plt.' + self.plot_type)(self.data_frame.eval(self.x_axis[column]),
                                          self.data_frame.eval(self.y_axis[0]))
        plt.title('Scraped Data')
        plt.ylabel(self.y_axis[0])
        x_label = ''
        for category in range(len(self.x_axis)):
            if category != len(self.x_axis)-1:
                x_label += self.x_axis[category] + ', '
            else:
                x_label += self.x_axis[category]
        plt.xlabel(x_label)
        plt.xticks(fontsize=7, rotation=10)
        plt.yticks(fontsize=7)
        plt.show()
'''


class DataVisualisation:

    def __init__(self, data_frame, categories, variables):
        self.data_frame = data_frame
        self.categories = categories
        self.variables = variables

    def construct_plot(self):
        plt.title('Scraped Data')
        plt.ylabel('Quantity')
        plt.xticks(fontsize=7, rotation=10)
        plt.yticks(fontsize=7)

        if len(self.categories) > 1:
            for c in range(len(self.categories)):
                eval('plt.bar')(self.data_frame.eval(self.categories[c]), self.data_frame.eval(self.variables[0]))
            x_label = ''
            for category in range(len(self.categories)):
                if category != len(self.categories) - 1:
                    x_label += self.categories[category] + ', '
                else:
                    x_label += self.categories[category]
            plt.xlabel(x_label)

        else:
            xpos = np.arange(len(self.data_frame.eval(self.categories[0])))
            plt.xticks(xpos, self.data_frame.eval(self.categories[0]))

            offset = 0.0
            for v in range(len(self.variables)):
                eval('plt.bar')(xpos+offset, self.data_frame.eval(self.variables[v]),
                                label=self.variables[v], width=0.05)
                offset += 0.055
            plt.legend(loc="upper right")

        plt.show()