import re


class Sorter:
    """
    Assigns tokens of DSQL input to correct variables to be passed to Reader class for distribution
    """
    #  Data structure for language components to be assigned to
    urls = []
    domains = []
    categories = []
    selectors = []
    modifiers = []
    response = ''
    page = ''
    rules = None
    conditions = {}
    where = []
    operators = []
    values = []
    logical_operators = []
    group_by = []
    aggregate_function = ''
    aggregate_operators = ''
    aggregate_value = []
    order = ''
    ascending = True
    cats = []
    vars = []

    def __init__(self, tokens):
        """
        Initialises class with tokens from instance of Lexer
        :param tokens: List of LexToken objects
        """
        self.tokens = tokens

    def remove_quotes(self, str):
        """
        Remove single and double quotes around strings from DSQL input
        :param str: LexToken value
        :return: String without quotes
        """
        return re.sub('[\'\"]', '', str)

    def flatten(self, lst):
        """
        Converts nested list to 1 dimensional list
        :param lst: nested list token value
        :return: 1 dimensional list
        """
        new_lst = []
        for i in lst:
            if type(i) != list:
                new_lst.append(i)
            else:
                new_lst.extend(i)
        return new_lst

    def is_number(self, string):
        """
        converts string value into float if the string only contains numerical characters
        :param string: token value
        :return: string if convertable and False boolean if not
        """
        try:
            float(string)
            return True
        except ValueError:
            return False

    def sort(self):
        """
        Processes all tokens from LexToken list, makes format adjustments to tokens and assigns them to correct
        data structure
        """
        # keywords for constructing rule dictionaries with eval()
        allow = 'allow'
        deny = 'deny'
        callback = 'callback'
        restrict_css = 'restrict_css'
        restrict_xpaths = 'restrict_xpaths'
        follow = 'follow'
        # loop for assigning components to variables
        for token in range(len(self.tokens)):
            if self.tokens[token].type == 'URL': self.urls.append(self.remove_quotes(self.tokens[token].value))
            if self.tokens[token].type == 'DOMAIN': self.domains.append(self.remove_quotes(self.tokens[token+2].value))
            if self.tokens[token].type == 'FIELD': self.categories.append(self.tokens[token].value)
            if self.tokens[token].type == 'SELECTOR' and self.tokens[token-1].type != 'EQUALS':
                self.selectors.append(self.remove_quotes(self.tokens[token].value))
                if self.tokens[token+1].type == 'MODIFIER':
                    self.modifiers.append(re.sub('[\(\) ]', '', str(self.tokens[token+1].value)).split(','))
                else:
                    self.modifiers.append([])
            if self.tokens[token-2].type == 'RESPONSE':
                self.response = self.remove_quotes(self.tokens[token].value)
            if self.tokens[token-2].type == 'PAGE':
                self.page = self.remove_quotes(self.tokens[token].value)
            if self.tokens[token].type == 'RULES':
                self.rules = eval(self.tokens[token].value)
            if self.tokens[token].type == 'FIELD' and \
                    (self.tokens[token-1].type == 'WHERE' or self.tokens[token-1].type == 'AND'):
                self.conditions[self.tokens[token].value] = (self.tokens[token+2].value, self.tokens[token+3].value)
            if self.tokens[token].type == 'COLUMN' and self.tokens[token - 1].type != 'GROUP_BY' and \
                    self.tokens[token - 1].type != 'ORDER_BY':
                self.where.append(self.tokens[token].value.strip('[]'))
            if self.tokens[token].type in {'EQUALS', 'GREATER', 'LESS', 'LESS_EQUAL', 'GREATER_EQUAL', 'NOT_EQUAL'} and \
                    self.tokens[token - 1].type == 'COLUMN': self.operators.append(self.tokens[token].type)
            if self.tokens[token].type in {'INTEGER', 'FLOAT', 'SELECTOR'} and \
                    self.tokens[token - 1].type in {'EQUALS', 'GREATER', 'LESS', 'LESS_EQUAL', 'GREATER_EQUAL', 'NOT_EQUAL'} \
                    and self.tokens[token - 2].type == 'COLUMN':
                self.values.append(self.remove_quotes(self.tokens[token].value))
            if self.tokens[token].type == 'AND' or self.tokens[token].type == 'OR':
                self.logical_operators.append(self.tokens[token].value)
            if self.tokens[token - 1].type == 'GROUP_BY':
                self.group_by.append(self.tokens[token].value.strip('[]').split(','))
                self.group_by = self.flatten(self.group_by)
                for j in range(len(self.group_by)):
                    self.group_by[j] = self.group_by[j].strip()
            if self.tokens[token - 1].type == 'HAVING': self.aggregate_function = self.tokens[token].value
            if self.tokens[token - 2].type == 'HAVING' and \
                    self.tokens[token].type in {'EQUALS', 'GREATER', 'LESS_EQUAL', 'GREATER_EQUAL', 'NOT_EQUAL'}:
                self.aggregate_operators = self.tokens[token].value
            if self.tokens[token - 3].type == 'HAVING' and \
                    self.tokens[token - 1].type in {'EQUALS', 'GREATER', 'LESS_EQUAL', 'GREATER_EQUAL', 'NOT_EQUAL'}:
                self.aggregate_value.append(self.tokens[token].value)
            if len(self.aggregate_value) > 0:
                if self.is_number(self.aggregate_value[0]):
                    self.aggregate_value[0] = float(self.aggregate_value[0])
            if self.tokens[token - 1].type == 'ORDER_BY':
                self.order = self.tokens[token].value.strip('[]')
            if self.tokens[token].type == 'DESCENDING':
                self.ascending = False
            if self.tokens[token - 2].type == 'CATS' and self.tokens[token].type == 'MODIFIER':
                self.cats.append(re.sub('[\(\) ]', '', str(self.tokens[token].value)).split(','))
                self.cats = self.flatten(self.cats)
            if self.tokens[token - 2].type == 'VARS' and self.tokens[token].type == 'MODIFIER':
                self.vars.append(re.sub('[\(\) ]', '', str(self.tokens[token].value)).split(','))
                self.vars = self.flatten(self.vars)



