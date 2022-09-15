import scrapy
from scrapy.crawler import CrawlerProcess
from DSQLScraper.DSQLScraper.items import DsqlscraperItem
#from dsqlspider.dsqlspider.items import sorter
from scrapy.loader import ItemLoader
from reader import r
import requests
import sys

'''
try:
    req = requests.get(r.urls)
    req.raise_for_status()
except requests.exceptions.HTTPError as err:
    print('Bad status code')
    sys.exit(1)
'''



class GenericSpider(scrapy.Spider):
    name = 'scrape'
    start_urls = r.urls

    def parse(self, response):
        if r.response.startswith('//'):
            res = response.xpath
        else:
            res = response.css

        for resp in res(r.response):
            loader = ItemLoader(item=DsqlscraperItem(), selector=resp)

            for i in range(len(r.categories)):
                loader.add_css(r.categories[i], r.selectors[i])

            yield loader.load_item()

        next_page = response.css(r.page).attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

