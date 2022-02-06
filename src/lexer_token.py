import re

def find_token_types(string):
    token_types = []
    for token_type in Token.__subclasses__():
        match = token_type.pattern.fullmatch(string)
        if match:
            token_types.append(token_type)
    return token_types

class Token(object):
    def __init__(self, value):
        pass

    def __repr__(self):
        if hasattr(self, "value"):
            return f"{self.__class__.__name__} {repr(self.value)}"
        else:
            return f"{self.__class__.__name__}"

    def __str__(self):
        return repr(self)

    def __bool__(self):
        return True

class Whitespace(Token):
    pattern = re.compile("[ \t]")
    def __bool__(self): return False

class Newline(Token):
    pattern = re.compile("\n")
    def __bool__(self): return False

class Comment(Token):
    pattern = re.compile("//.*")
    def __bool__(self): return False

class Name(Token):
    pattern = re.compile("[a-zA-Z_][a-zA-Z0-9_]*")
    def __init__(self, value): self.value: str = value

class Integer(Token):
    pattern = re.compile("[+-]?[0-9]+")
    def __init__(self, value): self.value: int = int(value)

class Character(Token):
    pattern = re.compile("'.*'")
    def __init__(self, value): self.value: int = value[0]

class Semicolon(Token): pattern = re.compile(";")
class Colon(Token):     pattern = re.compile(":")
class Comma(Token):     pattern = re.compile(",")
class Equals(Token):    pattern = re.compile("=")
class Plus(Token):      pattern = re.compile("\+")
class Minus(Token):     pattern = re.compile("-")
class Mul(Token):       pattern = re.compile("\*")
class Div(Token):       pattern = re.compile("/")
#class Arrow(Token):     pattern = re.compile("->")

class LParen(Token):    pattern = re.compile("\(")
class RParen(Token):    pattern = re.compile("\)")
class LSquare(Token):   pattern = re.compile("\[")
class RSquare(Token):   pattern = re.compile("\]")
class LCurly(Token):    pattern = re.compile("\{")
class RCurly(Token):    pattern = re.compile("\}")

class End:              pass
