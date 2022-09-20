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


def to_int(value):
    return int(re.sub('[^0-9]', '', value))


def strip_value(value):
    return value.strip()


class DsqlscraperItem(scrapy.Item):

    def __init__(self):
        super().__init__()

        for i in range(len(r.categories)):
            stipulations = []
            if 'clean' in r.modifiers[i]: stipulations.append(remove_tags)
            if 'float' in r.modifiers[i]: stipulations.append(to_float)
            elif 'int' in r.modifiers[i]: stipulations.append(to_int)
            else: stipulations.append(strip_value)
            self.fields[r.categories[i]] = scrapy.Field(input_processor=MapCompose(*stipulations),
                                                        output_processor=TakeFirst())


class CrawlspiderRuleMaker:

    rules = []
    allow_values = {}
    deny_values = {}
    callback_values = {}

    if r.rules:
        for i in range(len(r.rules)):
            for j in r.rules[i].keys():
                if j == 'allow':
                    allow_values[i] = r.rules[i][j]
                if j == 'deny':
                    deny_values[i] = r.rules[i][j]
                if j == 'callback':
                    callback_values[i] = r.rules[i][j]

        for i in range(len(r.rules)):
            allows = None
            denys = None
            callbacks = None
            if i in allow_values:
                allows = allow_values[i]
            if i in deny_values:
                denys = deny_values[i]
            if i in callback_values:
                callbacks = callback_values[i]
            rules.append(Rule(LinkExtractor(allow=allows, deny=denys), callback=callbacks))

    rules = tuple(rules)


#for i in range(len(r.rules)):
#    for j in r.rules[i].keys():
#        if j == 'allow':
            #allow_values[i] = r.rules[i][j]
#            print(r.rules[i][j])
#print(CrawlspiderRuleMaker.allow_values)
#print(CrawlspiderRuleMaker.deny_values)
#print(CrawlspiderRuleMaker.callback_values)
#rules2 = []
#d = {'allow': 'collections'}
#x = 'collections/japanese-whisky'

# extractor = LinkExtractor.