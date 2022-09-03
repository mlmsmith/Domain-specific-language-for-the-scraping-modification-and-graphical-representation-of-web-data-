from scrapy.crawler import CrawlerProcess
from DSQLScraper.DSQLScraper.spiders.genericSpider import GenericSpider
from DSQLScraper.DSQLScraper.spiders.crawlSpider import CrawlSpider
from dataManipulation import dm
import pandas as pd
from reader import r


process = CrawlerProcess(
    settings={
        'FEED_URI': 'data.csv',
        'FEED_FORMAT': 'csv',
        'FEED_OVERWRITE': True
    }
)


if len(r.rules) > 0:
    process.crawl(CrawlSpider)
    process.start()
else:
    process.crawl(GenericSpider)
    process.start()



#if len(r.where) > 0:
df = pd.read_csv('data.csv')
filtered_data = dm.filter_data(df, r.where, r.operators, r.values)#, r.logical_operators)
filtered_data.to_csv('data.csv')
    #aggregated_data = dm.group_by_having(df, r.group_by, r.aggregate_function, r.aggregate_operators, r.aggregate_value)
    #aggregated_data.to_csv('data.csv')
    #sorted_data = dm.order_by(aggregated_data, r.order, r.ascending)
    #sorted_data.to_csv('data.csv')


'''
df = pd.read_csv('data.csv')
f = Filterer(df)
filtered = f.concatinate_filters()
filtered.to_csv('filtered.csv')
'''


