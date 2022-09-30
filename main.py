import sys
import pandas.core.computation.ops
from scrapy.crawler import CrawlerProcess
from DSQLScraper.DSQLScraper.spiders.genericSpider import GenericSpider
from dataManipulation import dm
from dataVisualisation import DataVisualisation
import pandas as pd
from reader import r
import DSQLScraper.DSQLScraper.middlewares


#class Main:

def main():
    # clear previously scraped data from data.csv
    data = open('data.csv', 'w')
    data.truncate()
    data.close()
    # initialise CrawlerProcess
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
    # instantiate data frame
    try:
        df = pd.read_csv('data.csv')
    except pandas.errors.EmptyDataError:
        print('No data scraped')
        sys.exit(1)
    # check if data was successfully scraped
    if not len(df.index) > 1:#df.empty:
        print('No data scraped')
        sys.exit(1)
    # check if data filtering is specified
    if len(r.where) > 0:
        if len(r.logical_operators) > 0:
            df = dm.filter_data(df, r.where, r.operators, r.values, r.logical_operators)
        else:
            df = dm.filter_data(df, r.where, r.operators, r.values)
        df.to_csv('data.csv')
    # check if data aggregation is specified
    if len(r.group_by) > 0:
        if r.aggregate_function != '':
            if r.aggregate_operators != '' and len(r.aggregate_value) > 0:
                df = dm.group_by_having(df, r.group_by, r.aggregate_function, r.aggregate_operators, r.aggregate_value)
            else:
                df = dm.group_by_having(df, r.group_by, r.aggregate_function)
        else:
            df = dm.group_by_having(df, r.group_by)
        df.to_csv('data.csv')
    # check if data ordering is specified
    if r.order != '':
        if r.ascending:
            df = dm.order_by(df, r.order, True)
        else:
            df = dm.order_by(df, r.order, False)
        df.to_csv('data.csv')
    # check if graph is specified

    if len(r.cats) > 0:
        try:
            dv = DataVisualisation(df, r.cats, r.vars)
            dv.construct_plot()
        except pandas.core.computation.ops.UndefinedVariableError as err:
            print(err)


#if __name__ == '__main__':
#    main = Main()
#    main.run()
if __name__ == '__main__':
    main()
