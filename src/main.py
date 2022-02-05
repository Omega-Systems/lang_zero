from lexer import Lexer
from parser import Parser

def test():
    code = """
    fun main(arg0: int): int {
        // This is a comment
        var a: int = 2;
        var b: int = 3;
        var c: int = a + b;
    }
    """

    tokens = Lexer().lex(code)
    tree = Parser().parse(tokens)

if __name__ == '__main__':
    test()
