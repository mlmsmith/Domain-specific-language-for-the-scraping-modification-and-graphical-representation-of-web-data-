import scrapy
from scrapy.crawler import CrawlerProcess
from DSQLScraper.DSQLScraper.items import DsqlscraperItem
#from dsqlspider.dsqlspider.items import sorter
from scrapy.loader import ItemLoader
from reader import r
import requests
import sys


class GenericSpider(scrapy.Spider):
    name = 'scrape'
    start_urls = r.urls

    def parse(self, response):
        # check if response is a css or xpath selector
        if r.response.startswith('/') or r.response.startswith('./'):
            res = response.xpath
        else:
            res = response.css

        for resp in res(r.response):
            loader = ItemLoader(item=DsqlscraperItem(), selector=resp)

            for i in range(len(r.categories)):
                # check if category selector is css or xpath
                if r.selectors[i].startswith('/') or r.selectors[i].startswith('./'):
                    loader.add_xpath(r.categories[i], r.selectors[i])
                else:
                    loader.add_css(r.categories[i], r.selectors[i])

            yield loader.load_item()

        # check if page link is a css or xpath selector
        if r.page.startswith('/') or r.page.startswith('./'):
            next_page = response.xpath(r.page).attrib['href']
        elif r.page != '':
            next_page = response.css(r.page).attrib['href']
        # follow link to next webpage
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

