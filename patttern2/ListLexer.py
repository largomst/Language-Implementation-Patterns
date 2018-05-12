# LL(1) Recursive-Descent Lexer
from abc import abstractmethod


class Token:
    def __init__(self, type: int, text: str):
        self.type = type
        self.text = text

    def __str__(self):
        tname = ListLexer.tokenNames[self.type]
        return f"<'{self.text}', {tname}>"


class Lexer:
    EOF_TYPE = 1
    EOF = -1

    def __init__(self, input: str):
        self.input = input
        self.p = 0
        self.c = self.input[self.p]

    def consume(self):
        self.p += 1
        if self.p >= len(self.input):
            self.c = Lexer.EOF
        else:
            self.c = self.input[self.p]

    def match(self, x):
        if self.c == x:
            self.consume()
        else:
            raise Exception(f'excepting {x}; found c')

    @abstractmethod
    def nextToken(self): pass

    @abstractmethod
    def getTokenName(self): pass


class ListLexer(Lexer):

    NAME = 2
    COMMA = 3
    LBRACK = 4
    RBACK = 5

    tokenNames = [
        'n/a', '<EOF>', 'NAME', 'COMMA', 'LBRACK', 'RBRACK',
    ]

    @classmethod
    def getTokenName(cls, x: int):
        return cls.tokenNames[x]

    def isLETTTER(self):
        return 'a' <= self.c <= 'z' or 'A' <= self.c <= 'Z'

    def nextToken(self):
        while self.c != Lexer.EOF:
            if self.c in [' ', '\t', '\n', '\r']:
                self.WS()
            elif self.c == ',':
                self.consume()
                return Token(self.COMMA, ',')
            elif self.c == '[':
                self.consume()
                return Token(self.LBRACK, '[')
            elif self.c == ']':
                self.consume()
                return Token(self.RBACK, ']')
            else:
                if self.isLETTTER():
                    return self.NAME_()
                raise Exception('invalid character: ' + self.c)
        return Token(Lexer.EOF_TYPE, "<EOF>")

    def NAME_(self):
        buf = []
        while True:
            buf.append(self.c)
            self.consume()
            if not self.isLETTTER():
                break
        return Token(self.NAME, ''.join(buf))

    def WS(self):
        while self.c in [' ', '\t', '\n', '\r']:
            self.consume()
