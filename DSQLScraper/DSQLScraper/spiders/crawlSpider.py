import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from DSQLScraper.DSQLScraper.items import DsqlscraperItem, CrawlspiderRuleMaker
from scrapy.loader import ItemLoader
from reader import r


class Crawler(CrawlSpider):

    name = 'crawl'
    start_urls = r.urls
    allowed_domains = r.domains
    rules = CrawlspiderRuleMaker.rules

    def parse_item(self, response):

        loader = ItemLoader(item=DsqlscraperItem(), response=response)
        for category in range(len(r.categories)):

            if r.selectors[category].startswith('/') or r.selectors[category].startswith('./'):
                loader.add_xpath(r.categories[category], r.selectors[category])
            else:
                loader.add_css(r.categories[category], r.selectors[category])
        yield loader.load_item()









#print(len(Crawler.rules))
#print(Crawler.rules)
#print(Crawler.allow_values)
#print(Crawler.deny_values)
#print(Crawler.callback_values)

#for i in range(len(Crawler.rules)):
#    print(i+1, 'allow', Crawler.rules[i].link_extractor.allow_res)
#    print(i+1, 'deny', Crawler.rules[i].link_extractor.deny_res)
#    print(i+1, 'callback', Crawler.rules[i].callback)



