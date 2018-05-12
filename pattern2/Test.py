import sys
from ListLexer import *


def main():
    lexer = ListLexer(sys.argv[1])
    t = lexer.nextToken()
    while t.type != Lexer.EOF_TYPE:
        print(t)
        t = lexer.nextToken()
    print(t)


if __name__ == '__main__':
    main()
