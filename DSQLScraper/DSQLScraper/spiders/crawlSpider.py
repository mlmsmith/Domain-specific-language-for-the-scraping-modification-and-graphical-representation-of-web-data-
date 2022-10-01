import scrapy
from scrapy.spiders import CrawlSpider, Rule
from DSQLScraper.DSQLScraper.items import DsqlscraperItem, CrawlspiderRuleMaker
from scrapy.loader import ItemLoader
from reader import r


class Crawler(CrawlSpider):
    """
    Scrapes the intended website for the specified data according to the specified rules
    """
    name = 'crawl'
    start_urls = r.urls
    allowed_domains = r.domains
    rules = CrawlspiderRuleMaker.rules

    def parse_item(self, response):
        """
        Returns scraped data by processing the response from the website
        :param response: Response by website to request
        :return: Items of scraped data
        """
        loader = ItemLoader(item=DsqlscraperItem(), response=response)
        # Generate items of scraped data
        for category in range(len(r.categories)):
            # check if category selector is css or xpath
            if r.selectors[category].startswith('/') or r.selectors[category].startswith('./'):
                loader.add_xpath(r.categories[category], r.selectors[category])
            else:
                loader.add_css(r.categories[category], r.selectors[category])
        yield loader.load_item()










