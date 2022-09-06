from scrapy.crawler import CrawlerProcess
from DSQLScraper.DSQLScraper.spiders.genericSpider import GenericSpider
from dataManipulation import dm
from dataVisualisation import DataVisualisation
import pandas as pd
from reader import r


def main():
    # clear previously scraped data from csv
    data = open('data.csv', 'w')
    data.truncate()
    data.close()

    process = CrawlerProcess(
        settings={
            'FEED_URI': 'data.csv',
            'FEED_FORMAT': 'csv',
        }
    )
    # invoke correct spider class
    if r.rules:
        from DSQLScraper.DSQLScraper.spiders.crawlSpider import Crawler
        process.crawl(Crawler)
        process.start()
    else:
        process.crawl(GenericSpider)
        process.start()
    # check if data filtering is specified
    if len(r.where) > 0:
        df = pd.read_csv('data.csv')
        # check if multiple filters are specified
        if len(r.logical_operators) > 1:
            df = dm.filter_data(df, r.where, r.operators, r.values, r.logical_operators)
        else:
            df = dm.filter_data(df, r.where, r.operators, r.values)
        df.to_csv('data.csv')

    # check if data visualisation is specified
    #if r.plot_type != '':
    #    if len(r.where) > 0:
    #        date_frame = filtered_data
    #    else:
    #        data_frame = pd.read_csv('data.csv')
    #    dv = DataVisualisation(data_frame, r.plot_type, r.x_axis, r.y_axis)
    #    dv.construct_plot()

    dv = DataVisualisation(df, r.plot_type, r.x_axis, r.y_axis)
    dv.construct_plot()


if __name__ == '__main__':
    main()
