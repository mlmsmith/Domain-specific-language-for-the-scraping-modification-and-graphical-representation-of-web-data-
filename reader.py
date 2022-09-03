from compiler import MyLexer as Lexer
from compiler import MyParser as Parser_
from compiler import Sorter


class Reader:
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
    group_by = ''
    aggregate_function = ''
    aggregate_operators = ''
    aggregate_value = []
    order = ''
    ascending = bool

    def read(self):
        with open('src.dsl', 'r') as file:
            query = file.read().replace('\n', ' ')
        lexer = Lexer(query)
        lexer.build()
        lexer.test()

        tokens = lexer.tokens

        parser = Parser_(lexer, tokens)
        parser.build()
        parser.parser.parse(query)

        sorter = Sorter(lexer.t)
        sorter.sort()

        self.urls = sorter.urls
        self.domains = sorter.domains
        self.categories = sorter.categories
        self.selectors = sorter.selectors
        self.modifiers = sorter.modifiers
        self.response = sorter.response
        self.page = sorter.page
        self.rules = sorter.rules
        self.where = sorter.where
        self.operators = sorter.operators
        self.values = sorter.values
        self.logical_operators = sorter.logical_operators
        self.group_by = sorter.group_by
        self.aggregate_function = sorter.aggregate_function
        self.aggregate_operators = sorter.aggregate_operators
        self.aggregate_value = sorter.aggregate_value
        self.order = sorter.order
        self.ascending = sorter.ascending

r = Reader()
r.read()

'''
print('urls =', r.urls)
print('domains =', r.domains)
print('categories =', r.categories)
print('selectors =', r.selectors)
print('modifiers =', r.modifiers)
print('response =', r.response)
print('page =', r.page)
print('rules =', r.rules)
print('conditions =', r.conditions)
print('where =', r.where)
print('operators =', r.operators)
print('values =', r.values)
print('logical_operators =', r.logical_operators)
print('group_by =', r.group_by)
print('aggregate_function =', r.aggregate_function)
print('aggregate_operators =', r.aggregate_operators)
print('aggregate_value =', r.aggregate_value)
'''









#with open('src.dsl', 'r') as file:
    #query = file.read().replace('\n', ' ')
#

#l = Lexer(query)
#l.build()
#l.test()
#for i in l.t:
#    print(i)
#print()
