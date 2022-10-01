import sys

import ply.lex as lex


class Lexer:
    """
    Performs the tokenization of input and reports any notational errors
    """
    def __init__(self, DSQL):
        """
        Initialises class with the DSQL statement from user
        :param DSQL: input statement from src.dsl
        """
        self.DSQL = DSQL
    # LexerToken object to be appended to
    t = []
    # all token types
    tokens = [
        'SCRAPE',
        'CRAWL',
        'FIELD',
        'SELECTOR',
        'COLON',
        'MODIFIER',
        'URL',
        'DOMAIN',
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
        'RULES_LABEL',
        'RULES',
        'GROUP_BY',
        'HAVING',
        'AVERAGE',
        'SUM',
        'COUNT',
        'COLUMN',
        'ORDER_BY',
        'DESCENDING',
        'PLOT',
        'CATS',
        'VARS'
    ]
    # definitions for tokens
    t_SCRAPE = r'(?i)SCRAPE'
    t_CRAWL = r'(?i)CRAWL'
    t_FIELD = r'[A-Za-z]+(?=:)'
    t_SELECTOR = r'\'(.*?)\''
    t_MODIFIER = r'\((.*?)\)'
    t_URL = r'\'http(\S)+\''
    t_DOMAIN = r'(?i)DOMAIN'
    t_COLON = r'\:'
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
    t_GREATER = r'\>'
    t_LESS = r'\<'
    t_GREATER_EQUAL = r'\>\='
    t_LESS_EQUAL = r'\<\='
    t_NOT_EQUAL = r'\!\='
    t_RULES_LABEL = f'(?i)RULES'
    t_RULES = r'\[{(.*?)\}]'
    t_GROUP_BY = r'(?i)GROUP_BY'
    t_HAVING = r'(?i)HAVING'
    t_AVERAGE = r'(?i)AVG'
    t_SUM = r'(?i)SUM'
    t_COUNT = r'(?i)COUNT'
    t_COLUMN = r'\[(.*?)\]'
    t_ORDER_BY = r'(?i)ORDER_BY'
    t_DESCENDING = r'(?i)DESCENDING'
    t_PLOT = r'(?i)PLOT'
    t_CATS = r'(?i)CATS'
    t_VARS = r'(?i)VARS'
    t_ignore = r' '

    def t_error(self, t):
        """
        terminates tokenization if any input not defined by any token definitions is read
        :param t: token object
        :return: print statement to console
        """
        print('Invalid input')
        sys.exit(1)

    def build(self):
        self.lexer = lex.lex(module=self)

    def tokenize(self):
        """
        performs identification and assigning of each component to correct token type
        :return: list of LexToken objects
        """
        self.lexer.input(self.DSQL)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            self.t.append(tok)
