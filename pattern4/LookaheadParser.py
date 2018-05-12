# LL(k) Recursive-Descent Parser
from LookaheadLexer import LookaheadLexer
from Parser import Parser


class LookaheadParser(Parser):

    def list_(self):
        self.match(LookaheadLexer.LBRACK)
        self.elements()
        self.match(LookaheadLexer.RBACK)

    def elements(self):
        self.element()
        while self.LA(1) == LookaheadLexer.COMMA:
            self.match(LookaheadLexer.COMMA)
            self.element()

    def element(self):
        if self.LA(1) == LookaheadLexer.NAME and self.LA(2) == LookaheadLexer.EQUALS:
            self.match(LookaheadLexer.NAME)
            self.match(LookaheadLexer.EQUALS)
            self.match(LookaheadLexer.NAME)
        elif self.LA(1) == LookaheadLexer.NAME:
            self.match(LookaheadLexer.NAME)
        elif self.LA(1) == LookaheadLexer.LBRACK:
            self.list_()
        else:
            raise Exception(f"expecting name or list; found {self.LT(1)}")
