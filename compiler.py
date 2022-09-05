import ply.lex as lex
import ply.yacc as yacc
import re


class MyLexer:
    def __init__(self, DSQL):
        self.DSQL = DSQL
    t = []
    tokens = [
        'SCRAPE',
        'CRAWL',
        'FIELD',
        # 'NAME',
        'SELECTOR',
        'COLON',
        'MODIFIER',
        'URL',
        'L_BRACKET',
        'R_BRACKET',
        'COMMA',
        'FROM',
        'WHERE',
        'AND',
        'OR',
        'EQUALS',
        'GREATER',
        'LESS',
        'GREATER_EQUAL',
        'LESS_EQUAL',
        'NOT_EQUAL',
        'RESPONSE',
        'PAGE',
        'INTEGER',
        'FLOAT',
        # 'STRING',
        'RULES_LABEL',
        'RULE',
        'GROUP_BY',
        'HAVING',
        'AVERAGE',
        'SUM',
        'COUNT',
        # 'WORD',
        'COLUMN',
        'ORDER_BY',
        'DESCENDING',
        'BAR_PLOT',
        'LINE_PLOT',
        'X',
        'Y'
    ]

    t_SCRAPE = r'(?i)SCRAPE'
    t_CRAWL = r'(?i)CRAWL'
    t_FIELD = r'[A-Za-z]+(?=:)'
    # t_NAME = r'[A-Za-z]+(?!=:)'
    t_SELECTOR = r'\'(.*?)\''
    t_MODIFIER = r'\((.*?)\)'
    t_URL = r'\'http(.+?)\''
    t_COLON = r'\:'
    t_L_BRACKET = r'\['
    t_R_BRACKET = r'\]'
    t_COMMA = r'\,'
    t_FROM = r'(?i)FROM'
    t_WHERE = r'(?i)WHERE'
    t_AND = r'(?i)AND'
    t_OR = r'(?i)OR'
    t_EQUALS = r'\='
    t_RESPONSE = r'(?i)RESPONSE'
    t_PAGE = r'(?i)PLINK'
    t_INTEGER = r'\d+'
    t_FLOAT = r'\d+(\.)\d+'
    # t_STRING = r'\(\'.+?\'\)'
    t_GREATER = r'\>'
    t_LESS = r'\<'
    t_GREATER_EQUAL = r'\>\='
    t_LESS_EQUAL = r'\<\='
    t_NOT_EQUAL = r'\!\='
    t_RULES_LABEL = f'(?i)RULES'
    t_RULE = r'\{(.*?)\}'
    t_GROUP_BY = r'(?i)GROUP_BY'
    t_HAVING = r'(?i)HAVING'
    t_AVERAGE = r'(?i)AVG'
    t_SUM = r'(?i)SUM'
    t_COUNT = r'(?i)COUNT'
    # t_WORD = r'(?<=WHERE)[A-Za-z]+'
    t_COLUMN = r'\[(.*?)\]'
    t_ORDER_BY = r'(?i)ORDER_BY'
    t_DESCENDING = r'(?i)DESCENDING'
    t_BAR_PLOT = r'(?i)BAR_PLOT'
    t_LINE_PLOT = r'(?i)LINE_PLOT'
    t_X = r'(?i)X( )*=( )*'
    t_Y = r'(?i)Y( )*=( )*'
    t_ignore = r' '


    #reserved = {
    #    'from': 'FROM',
    #    'where': 'WHERE',
    #    'and': 'AND'
    #}

    def t_error(self, t):
        print('Invalid input')

    def build(self):
        self.lexer = lex.lex(module=self)

    def test(self):
        self.lexer.input(self.DSQL)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            self.t.append(tok)
            print(tok)



class MyParser:

    def __init__(self, lexer, tokens):
        self.lexer = lexer
        self.tokens = tokens
        self.parser = yacc.yacc(module=self)

    def build(self):
        self.parser = yacc.yacc(module=self)

    def p_statement(self, p):
        '''
        statement      : scrape
                       | crawl
        scrape         : SCRAPE categories location response page manipulation sorting plot
                       | location SCRAPE categories response page manipulation sorting plot
        crawl          : CRAWL categories crawl_location response instructions manipulation sorting plot
                       | crawl_location CRAWL categories response instructions manipulation sorting plot
        categories     : category
                       | category COMMA categories
        category       : FIELD COLON SELECTOR MODIFIER
                       | FIELD COLON SELECTOR
        location       : FROM URL
        crawl_location : FROM URL COMMA SELECTOR
        response       : RESPONSE EQUALS SELECTOR
        page           : PAGE EQUALS SELECTOR
                       |
        instructions   : RULES_LABEL EQUALS L_BRACKET rules R_BRACKET
        rules          : RULE
                       | RULE COMMA rules
        manipulation   : filtering aggregation
                       | filtering
                       |
        filtering      : WHERE conditions
        conditions     : condition
                       | condition AND conditions
                       | condition OR conditions
        condition      : COLUMN operator INTEGER
                       | COLUMN operator FLOAT
                       | COLUMN EQUALS SELECTOR
        operator       : EQUALS
                       | GREATER
                       | LESS
                       | GREATER_EQUAL
                       | LESS_EQUAL
                       | NOT_EQUAL
        aggregation    : GROUP_BY COLUMN
                       | GROUP_BY COLUMN HAVING aggregate
                       | GROUP_BY COLUMN HAVING aggregate operator INTEGER
                       | GROUP_BY COLUMN HAVING aggregate operator FLOAT
        aggregate      : AVERAGE
                       | SUM
                       | COUNT
        sorting        : ORDER_BY COLUMN
                       | ORDER_BY COLUMN DESCENDING
                       |
        plot           : BAR_PLOT x_axis COMMA y_axis
                       | LINE_PLOT x_axis COMMA y_axis
                       |
        x_axis         : X MODIFIER
        y_axis         : Y MODIFIER
        '''



class Sorter:
    urls = []
    domains = []
    categories = []
    selectors = []
    modifiers = []
    response = ''
    page = ''
    rules = []
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


    def __init__(self, tokens):
        self.tokens = tokens

    def remove_quotes(self, str):
        return re.sub('[\'\"]', '', str)

    def flatten(self, l):
        return [item for sublist in l for item in sublist]

    #def flatten(self, lst):
    #    new_lst = []
    #    for i in lst:
    #        if type(i) != list:
    #            new_lst.append(i)
    #        else:
    #            new_lst.extend(i)
    #    return new_lst

    def is_number(self, str):
        try:
            float(str)
            return True
        except ValueError:
            return False

    def sort(self):
        for token in range(len(self.tokens)):
            # add URLs, fields and their selectors and modifiers
            if self.tokens[token].type == 'URL': self.urls.append(self.remove_quotes(self.tokens[token].value))
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
            if self.tokens[token].type == 'RULE':
                self.rules.append(eval(self.tokens[token].value))
            if self.tokens[token].type == 'FIELD' and \
                    (self.tokens[token-1].type == 'WHERE' or self.tokens[token-1].type == 'AND'):
                self.conditions[self.tokens[token].value] = (self.tokens[token+2].value, self.tokens[token+3].value)
            if self.tokens[token].type == 'RULE': self.rules.append(self.tokens[token].value)
            if self.tokens[token].type == 'COLUMN' and self.tokens[token - 1].type != 'GROUP_BY':
                self.where.append(self.tokens[token].value.strip('[]'))
            if self.tokens[token].type in {'EQUALS', 'GREATER', 'LESS_EQUAL', 'GREATER_EQUAL', 'NOT_EQUAL'} and \
                    self.tokens[token - 1].type == 'COLUMN': self.operators.append(self.tokens[token].type)
            if self.tokens[token].type in {'INTEGER', 'FLOAT', 'SELECTOR'} and \
                    self.tokens[token - 1].type in {'EQUALS', 'GREATER', 'LESS_EQUAL', 'GREATER_EQUAL', 'NOT_EQUAL'} \
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



#with open('src.dsl', 'r') as file:
#    query = file.read().replace('\n', ' ')


#l = MyLexer(query)
#l.build()
#l.test()

#p = MyParser(l, l.tokens)

#p.build()

#p.parser.parse(query)
'''
s = Sorter(l.t)
s.sort()


print('s urls', s.urls)
print('s domains', s.domains)
print('s categories', s.categories)
print('s selectors', s.selectors)
print('s modifiers', s.modifiers)
print('s response', s.response)
print('s page', s.page)
print('s rules', s.rules)
print('s conditions', s.conditions)
print('s where', s.where)
print('s operators', s.operators)
print('s values', s.values)
print('s logical_operators', s.logical_operators)
print('s group_by', s.group_by)
print('s aggregate_function', s.aggregate_function)
print('s aggregate_operators', s.aggregate_operators)
print('s aggregate_value', s.aggregate_value)
print('s order', s.order)
print('s ascending', s.ascending)
'''






















