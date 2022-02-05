from lexer import Lexer
from parser import Parser

def test():
    code = """
    {
        // Eins Kommentar
        var bostel_stinkt: bool = 1;
    }
    """

    tokens = Lexer().lex(code)
    tree = Parser().parse(tokens)

if __name__ == '__main__':
    test()
