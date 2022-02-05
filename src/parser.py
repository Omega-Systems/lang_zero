import lexer_token as token
import parser_node as node

class Parser:
    def __init__(self):
        pass

    def parse(self, tokens):
        print(f"=== STARTING PARSING ===")
        self.tokens = iter(tokens)
        self.current_token = next(self.tokens)
        #print(self.current_token)
        tree = self.parse_compound()
        tree.output()
        print(f"=== FINISHED PARSING ===")
        print()
        return tree

    def parse_compound(self):
        statements = []
        self.consume(token.LCurly)
        while type(self.current_token) != token.RCurly:
            #print(self.current_token)
            statement = self.parse_statement()
            statements.append(statement)
        #self.consume(token.RParen)
        return node.Compound(statements)

    def parse_statement(self):
        match type(self.current_token):
            case token.Name:
                match self.current_token.value:
                    case "var":
                        self.consume(token.Name)
                        name = self.parse_name()
                        self.consume(token.Colon)
                        datatype = self.parse_name()
                        self.consume(token.Equals)
                        value = self.parse_sum()
                        self.consume(token.Semicolon)
                        return node.VarDeclaration(name, datatype, value)

    def parse_name(self):
        return node.Identifier(self.consume(token.Name))

    def parse_sum(self):
        new_node = self.parse_product()
        while type(self.current_token) in (token.Plus, token.Minus):
            new_node = node.BinaryOp(
                self.consume(token.Plus, token.Minus),
                new_node,
                self.parse_product())
        return new_node

    def parse_product(self):
        new_node = self.parse_factor()
        while type(self.current_token) in (token.Mul, token.Div):
            new_node = node.BinaryOp(
                self.consume(token.Mul, token.Div),
                new_node,
                self.parse_factor())
        return new_node

    def parse_factor(self):
        match type(self.current_token):
            case token.Integer:
                return node.Integer(self.consume(token.Integer))
            case token.Name:
                return node.Identifier(self.consume(token.Name))
            case token.Plus:
                return node.UnaryOp(self.consume(token.Plus), self.parse_factor())
            case token.Minus:
                return node.UnaryOp(self.consume(token.Minus), self.parse_factor())
            case token.LParen:
                self.consume(token.LParen)
                new_node = self.parse_sum()
                self.consume(token.RParen)
                return new_node
        raise Exception(f"Invalid syntax near {repr(self.current_token)}")

    def consume(self, *token_types):
        if type(self.current_token) in token_types:
            last_token = self.current_token
            self.current_token = next(self.tokens)
            return last_token
        else:
            raise Exception(f"Invalid syntax")
