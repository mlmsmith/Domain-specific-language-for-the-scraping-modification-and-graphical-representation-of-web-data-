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

        for category in range(len(r.categories)):
            for res in response.css(r.selectors[category]):
                loader = ItemLoader(item=DsqlscraperItem(), selector=res)
                loader.add_css(r.categories[category], r.selectors[category])

                yield loader.load_item()

    '''
    rules = []
    allow_values = {}
    deny_values = {}
    callback_values = {}

    for i in range(len(r.rules)):
        for j in r.rules[i].keys():
            if j == 'allow':
                allow_values[i] = r.rules[i][j]
            if j == 'deny':
                deny_values[i] = r.rules[i][j]
            if j == 'callback':
                callback_values[i] = r.rules[i][j]

    for i in range(len(r.rules)):
        allows = []
        denys = []
        callbacks = []
        if i in allow_values:
            allows.append(allow_values[i])
        if i in deny_values:
            denys.append(deny_values[i])
        if i in callback_values:
            callbacks.append(callback_values[i])
        rules.append(Rule(LinkExtractor(allow=allows, deny=denys), callback=callbacks))

    rules = tuple(rules)
    
    rules = [
        Rule(LinkExtractor(allow='collections/japanese-whisky', deny='products')),
        Rule(LinkExtractor(allow='products'), callback='parse_item')
    ]
    '''









#print(len(Crawler.rules))
#print(Crawler.rules)
#print(Crawler.allow_values)
#print(Crawler.deny_values)
#print(Crawler.callback_values)

#for i in range(len(Crawler.rules)):
#    print(i+1, 'allow', Crawler.rules[i].link_extractor.allow_res)
#    print(i+1, 'deny', Crawler.rules[i].link_extractor.deny_res)
#    print(i+1, 'callback', Crawler.rules[i].callback)



