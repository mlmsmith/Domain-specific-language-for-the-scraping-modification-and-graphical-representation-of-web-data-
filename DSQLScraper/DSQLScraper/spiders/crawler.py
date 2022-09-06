import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.crawler import CrawlerProcess


class SipSpider(CrawlSpider):
    name = 'sip'
    allowed_domains = ['sipwhiskey.com']
    start_urls = ['http://sipwhiskey.com/']

    rules = [
        Rule(LinkExtractor(allow='collections/japanese-whisky', deny='products')),
        Rule(LinkExtractor(allow='products'), callback='parse_item')
    ]

    def parse_item(self, response):
        yield {
            'brand': response.css('div.vendor a::text').get(),
            'name': response.css('h1.title::text').get(),
            'price': response.css('span.price::text').get()
        }


process = CrawlerProcess(
    settings={
        'FEED_URI': 'data.csv',
        'FEED_FORMAT': 'csv',
    }
)


process.crawl(SipSpider)
process.start()