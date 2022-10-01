import attr
import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose
from w3lib.html import remove_tags
import re
from reader import r
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule


# modification functions
def to_float(value):
    return float(re.sub('[^\d\.]', '', value))


def to_int(value):
    return int(re.sub('[^0-9]', '', value))


def strip_value(value):
    return value.strip()


def capitalise(value):
    return value.capitalize()


def upper_case(value):
    return value.upper()


def lower_case(value):
    return value.lower()


def replace_spaces(value):
    return '_'.join(value.split())


class DsqlscraperItem(scrapy.Item):
    """
    Creates items of scraped data and modifies the data within before passing to spider classes
    """
    def __init__(self):
        """
        Initialises class by inheriting fields dictionary from Item class
        """
        super().__init__()
        # assigns appropriate data modification functions to each Field object before adding to fields dictionary
        for i in range(len(r.categories)):
            stipulations = []
            if 'clean' in r.modifiers[i]: stipulations.append(remove_tags)
            if 'upper' in r.modifiers[i]: stipulations.append(upper_case)
            if 'lower' in r.modifiers[i]: stipulations.append(lower_case)
            if 'cap' in r.modifiers[i]: stipulations.append(capitalise)
            if 'nospace' in r.modifiers[i]: stipulations.append(replace_spaces)
            if 'float' in r.modifiers[i]: stipulations.append(to_float)
            elif 'int' in r.modifiers[i]: stipulations.append(to_int)
            else: stipulations.append(strip_value)
            self.fields[r.categories[i]] = scrapy.Field(input_processor=MapCompose(*stipulations),
                                                        output_processor=TakeFirst())


class CrawlspiderRuleMaker:
    """
    Creates tuple of Rule objects to be passed to CrawlSpider
    """
    rules = []
    allow_values = {}
    deny_values = {}
    restrict_css_values = {}
    restrict_xpath_values = {}
    callback_values = {}
    follow_values = {}
    # Add values to be processed by each Rule parameter with the index at which they should be in the Rule object
    if r.rules:
        for i in range(len(r.rules)):
            for j in r.rules[i].keys():
                if j == 'allow':
                    allow_values[i] = r.rules[i][j]
                if j == 'deny':
                    deny_values[i] = r.rules[i][j]
                if j == 'callback':
                    callback_values[i] = r.rules[i][j]
                if j == 'restrict_css':
                    restrict_css_values[i] = r.rules[i][j]
                if j == 'restrict_xpath':
                    restrict_xpath_values[i] = r.rules[i][j]
                if j == 'follow':
                    follow_values[i] = r.rules[i][j]
        # Add function parameters in the correct order to Rule objects
        for i in range(len(r.rules)):
            allows = None
            denys = None
            restrict_c = None
            restrict_x = None
            callbacks = None
            follows = None
            if i in allow_values:
                allows = allow_values[i]
            if i in deny_values:
                denys = deny_values[i]
            if i in restrict_css_values:
                restrict_c = restrict_css_values[i]
            if i in restrict_xpath_values:
                restrict_x = restrict_xpath_values[i]
            if i in callback_values:
                callbacks = callback_values[i]
            if i in follow_values:
                follows = follow_values[i]

            rules.append(Rule(LinkExtractor(allow=allows, deny=denys, restrict_css=restrict_c,
                                            restrict_xpaths=restrict_x), callback=callbacks, follow=follows))

    rules = tuple(rules)

