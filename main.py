from scrapy.crawler import CrawlerProcess
from DSQLScraper.DSQLScraper.spiders.genericSpider import GenericSpider
from DSQLScraper.DSQLScraper.spiders.crawlSpider import CrawlSpider
from dataManipulation import dm
from dataVisualisation import DataVisualisation
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
dv = DataVisualisation(filtered_data, r.plot_type, r.x_axis, r.y_axis)
dv.construct_plot()

