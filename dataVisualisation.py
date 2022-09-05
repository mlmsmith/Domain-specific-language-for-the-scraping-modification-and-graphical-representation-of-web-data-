import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pylab as pl


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

