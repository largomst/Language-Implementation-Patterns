from typing import List

from LookaheadLexer import LookaheadLexer, Token


class Parser:
    def __init__(self, input: LookaheadLexer, k: int):
        self.input = input
        self.k = k
        self.lookahead: List[Token] = [None] * k
        self.p = 0
        for i in range(k):
            self.consume()

    def consume(self):
        self.lookahead[self.p] = self.input.nextToken()
        self.p = (self.p + 1) % self.k

    def LT(self, i: int) -> Token:
        return self.lookahead[(self.p + i - 1) % self.k]

    def LA(self, i: int) -> int:
        return self.LT(i).type

    def match(self, x: int):
        if self.LA(1) == x:
            self.consume()
        else:
            raise Exception(f"expecting {self.input.getTokenName(x)}; found {self.LT(1)}")


