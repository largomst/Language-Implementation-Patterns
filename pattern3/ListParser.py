# LL(1) Recursive-Descent Parser
from ListLexer import Lexer, ListLexer


class Parser:
    def __init__(self, input: Lexer):
        self.input = input
        self.lookahead = self.input.nextToken()

    def match(self, x: int):
        if self.lookahead.type == x:
            self.consume()
        else:
            raise Exception(
                f'expecting {self.input.getTokenName(x)}; found {self.lookahead}')

    def consume(self):
        self.lookahead = self.input.nextToken()


class ListParser(Parser):

    def list_(self):
        self.match(ListLexer.LBRACK)
        self.elements()
        self.match(ListLexer.RBACK)

    def elements(self):
        self.element()
        while self.lookahead.type == ListLexer.COMMA:
            self.match(ListLexer.COMMA)
            self.element()

    def element(self):
        if self.lookahead.type == ListLexer.NAME:
            self.match(ListLexer.NAME)
        elif self.lookahead.type == ListLexer.LBRACK:
            self.list_()
        else:
            raise Exception(f"expecting name or list; found {self.lookahead}")
