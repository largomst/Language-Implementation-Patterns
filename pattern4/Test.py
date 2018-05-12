import sys

from LookaheadLexer import LookaheadLexer
from LookaheadParser import LookaheadParser


def main():
    lexer = LookaheadLexer(sys.argv[1])
    parser = LookaheadParser(lexer, 2)
    parser.list_()


if __name__ == '__main__':
    main()
