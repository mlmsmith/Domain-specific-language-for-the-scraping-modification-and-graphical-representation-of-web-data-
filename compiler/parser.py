import ply.yacc as yacc
import sys


class Parser_:
    """
    Generates abstract syntax tree of DSQL statement and catches syntactic errors
    """
    def __init__(self, lexer, tokens):
        """
        Initialises class with instance of PLY yacc tool
        :param lexer: lexer created in build() method of Lexer class
        :param tokens:
        """
        self.lexer = lexer
        self.tokens = tokens

    def build(self):
        """
        Creates parser using PLY yacc tool
        :return: parser object
        """
        self.parser = yacc.yacc(module=self)

    def p_statement(self, p):  # definition of language syntax in BNF
        """
        statement      : scrape
                       | crawl
        scrape         : SCRAPE categories location response page manipulation sorting plot
        crawl          : CRAWL categories location instructions manipulation sorting plot
        categories     : category
                       | category COMMA categories
        category       : FIELD COLON SELECTOR MODIFIER
                       | FIELD COLON SELECTOR
        location       : FROM URL
                       | FROM URL domain
        domain         : DOMAIN EQUALS SELECTOR
        response       : RESPONSE EQUALS SELECTOR
        page           : PAGE EQUALS SELECTOR
                       |
        instructions   : RULES_LABEL EQUALS RULES
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
        plot           : PLOT cats COMMA vars
                       |
        cats           : CATS EQUALS MODIFIER
        vars           : VARS EQUALS MODIFIER
        """

    def p_error(self, p):
        """
        Catches and reports syntactic errors in DSQL statement
        :param p: parser object RR
        :return: Print statement to console
        """
        print('invalid syntax')
        sys.exit(1)
