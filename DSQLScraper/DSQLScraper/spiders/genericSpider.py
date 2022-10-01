import scrapy
from DSQLScraper.DSQLScraper.items import DsqlscraperItem
from scrapy.loader import ItemLoader
from reader import r


class GenericSpider(scrapy.Spider):
    """
    Scrapes the intended website for the specified data
    """
    name = 'scrape'
    start_urls = r.urls

    def parse(self, response):
        """
        Returns scraped data by processing the response from the website
        :param response: Response by website to request
        :return: Items of scraped data
        """
        # check if response is a css or xpath selector
        if r.response.startswith('/') or r.response.startswith('./'):
            res = response.xpath
        else:
            res = response.css
        # Generate items of scraped data
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

