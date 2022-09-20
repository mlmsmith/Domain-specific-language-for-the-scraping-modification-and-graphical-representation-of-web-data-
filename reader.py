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
    #plot_type = ''
    cats = []
    vars = []

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
        #self.plot_type = sorter.plot_type
        self.cats = sorter.cats
        self.vars = sorter.vars


r = Reader()
try:
    r.read()
except Exception:
    ('bad input')


print('r urls =', r.urls)
print('r domains =', r.domains)
print('r categories =', r.categories)
print('r selectors =', r.selectors)
print('r modifiers =', r.modifiers)
print('r response =', r.response)
print('r page =', r.page)
print('r rules =', r.rules)
print('r conditions =', r.conditions)
print('r where =', r.where)
print('r operators =', r.operators)
print('r values =', r.values)
print('r logical_operators =', r.logical_operators)
print('r group_by =', r.group_by)
print('r aggregate_function =', r.aggregate_function)
print('r aggregate_operators =', r.aggregate_operators)
print('r aggregate_value =', r.aggregate_value)
print('r order =', r.order)
print('r ascending =', r.ascending)
#print('r plot type =', r.plot_type)
print('r cats =', r.cats)
print('r vars =', r.vars)













#with open('src.dsl', 'r') as file:
    #query = file.read().replace('\n', ' ')
#

#l = Lexer(query)
#l.build()
#l.test()
#for i in l.t:
#    print(i)
#print()
