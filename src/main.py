from lexer import Lexer
from parser import Parser

def test():
    code = """
    fun calculate(x: int): int {
        var x_squared: int = x * x;
        return 2 * x_squared;
    }
    """

    tokens = Lexer().lex(code)
    tree = Parser().parse(tokens)

if __name__ == '__main__':
    test()
