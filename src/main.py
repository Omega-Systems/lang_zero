from lexer import Lexer
from parser import Parser

def test():
    code = """
    fun calculate(x: int): int {
        var y: int = 3 * x;
        return y;
    }
    """

    tokens = Lexer().lex(code)
    tree = Parser().parse(tokens)

if __name__ == '__main__':
    test()
