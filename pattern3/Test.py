import sys
from ListLexer import ListLexer
from ListParser import ListParser


def main():
    lexer = ListLexer(sys.argv[1])
    parser = ListParser(lexer)
    parser.list_()


if __name__ == '__main__':
    main()
