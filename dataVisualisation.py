import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import pylab as pl


class DataVisualisation:
    """
    Generates bar chart depicting scraped data
    """
    def __init__(self, data_frame, categories, variables):
        """
        Initialises class with stipulations made about the layout of the graph
        :param data_frame: Pandas data frame of scraped data from data.csv
        :param categories: Categories from data to be included in the graph
        :param variables: Variables from data to be included in the graph
        """
        self.data_frame = data_frame
        self.categories = categories
        self.variables = variables

    def construct_plot(self):
        """
        Build and display specified plot
        :return:
        """
        plt.title('Scraped Data')
        plt.ylabel('Quantity')
        plt.xticks(fontsize=7, rotation=10)
        plt.yticks(fontsize=7)
        # Determine which type of plot to be constructed: multiple categories or multiple varialbes
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
            # add each bar with offset to avoid overlap
            for v in range(len(self.variables)):
                eval('plt.bar')(xpos+offset, self.data_frame.eval(self.variables[v]),
                                label=self.variables[v], width=0.05)
                offset += 0.055
            plt.legend(loc="upper right")
        plt.show()
