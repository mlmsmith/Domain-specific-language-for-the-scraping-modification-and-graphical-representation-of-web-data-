import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from DSQLScraper.DSQLScraper.items import DsqlscraperItem
from scrapy.loader import ItemLoader
from reader import r


class Crawler(CrawlSpider):
    pass
    '''
        name = 'crawl'
    start_urls = r.urls
    allowed_domains = r.domains

    def parse_item(self, response):

        if r.response.startswith('//'):
            res = response.xpath
        else:
            res = response.css

        for resp in res(r.response):
            loader = ItemLoader(item=DsqlspiderItem(), selector=resp)

            for i in range(len(r.categories)):
                loader.add_css(r.categories[i], r.selectors[i])

            yield loader.load_item()

    '''



