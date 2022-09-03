import attr
import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags
import re
from reader import r
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


def to_float(value):
    return float(re.sub('[^\d\.]', '', value))


class DsqlscraperItem(scrapy.Item):

    def __init__(self):
        super().__init__()

        for i in range(len(r.categories)):
            stipulations = []
            if 'clean' in r.modifiers[i]: stipulations.append(remove_tags)
            if 'float' in r.modifiers[i]: stipulations.append(to_float)
            self.fields[r.categories[i]] = scrapy.Field(input_processor=MapCompose(*stipulations),
                                                        output_processor=TakeFirst())


rules2 = []
d = {'allow': 'collections'}
x = 'collections/japanese-whisky'

# extractor = LinkExtractor.