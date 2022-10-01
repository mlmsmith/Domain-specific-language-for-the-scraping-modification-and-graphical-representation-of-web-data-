from compiler.lexer import Lexer
from compiler.parser import Parser_
from compiler.sorter import Sorter


class Reader:
    """
    Read in input from dsl.sql, invokes compilation of input and takes the variables created in Sorter to be imported
    into other areas of the program
    """
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
    cats = []
    vars = []

    def read(self):
        """
        Reads in DSQL input, ignoring lines beginning with '#'
        :return: String of input
        """
        query = ''  # input added to query string
        with open('src.dsl', 'r') as file:
            for line in file:
                if line[0] != '#':
                    query += line.replace('\n', ' ')
        # Instantiate compiler classes
        lexer = Lexer(query)
        lexer.build()
        lexer.tokenize()

        tokens = lexer.tokens

        parser = Parser_(lexer, tokens)
        parser.build()
        parser.parser.parse(query)

        sorter = Sorter(lexer.t)
        sorter.sort()
        # Assign Sorter variables to Reader
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
        self.cats = sorter.cats
        self.vars = sorter.vars


# Instantiate Reader class in current file to avoid circular import issues
r = Reader()
try:
    r.read()
except Exception as err:
    print(err)


