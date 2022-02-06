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
        tree = self.parse_function()
        print()
        tree.output()
        print(f"=== FINISHED PARSING ===")
        print()
        return tree

    def parse_function(self):
        self.match(token.Name)
        name = self.parse_name()
        self.match(token.LParen)
        arguments = []
        while type(self.current_token) != token.RParen:
            argname = self.parse_name()
            self.match(token.Colon)
            datatype = self.parse_name()
            arguments.append(node.Variable(argname, datatype))
        self.match(token.RParen)
        self.match(token.Colon)
        return_type = self.parse_name()
        body = self.parse_compound()
        return node.Function(name, arguments, return_type, body)

    def parse_compound(self):
        statements = []
        self.match(token.LCurly)
        while type(self.current_token) != token.RCurly:
            statement = self.parse_statement()
            statements.append(statement)
        self.match(token.RCurly)
        return node.Compound(statements)

    def parse_statement(self):
        match type(self.current_token):
            case token.Name:
                match self.current_token.value:
                    case "var":
                        self.match(token.Name)
                        name = self.parse_name()
                        self.match(token.Colon)
                        datatype = self.parse_name()
                        self.match(token.Equals)
                        value = self.parse_sum()
                        self.match(token.Semicolon)
                        variable = node.Variable(name, datatype)
                        return node.VarDeclaration(variable, value)
                    case "return":
                        self.match(token.Name)
                        value = self.parse_sum()
                        self.match(token.Semicolon)
                        return node.Return(value)

    def parse_name(self):
        return node.Identifier(self.match(token.Name))

    def parse_sum(self):
        new_node = self.parse_product()
        while type(self.current_token) in (token.Plus, token.Minus):
            new_node = node.BinaryOp(
                self.match(token.Plus, token.Minus),
                new_node,
                self.parse_product())
        return new_node

    def parse_product(self):
        new_node = self.parse_factor()
        while type(self.current_token) in (token.Mul, token.Div):
            new_node = node.BinaryOp(
                self.match(token.Mul, token.Div),
                new_node,
                self.parse_factor())
        return new_node

    def parse_factor(self):
        match type(self.current_token):
            case token.Integer:
                return node.Integer(self.match(token.Integer))
            case token.Name:
                return node.Identifier(self.match(token.Name))
            case token.Plus:
                return node.UnaryOp(self.match(token.Plus), self.parse_factor())
            case token.Minus:
                return node.UnaryOp(self.match(token.Minus), self.parse_factor())
            case token.LParen:
                self.match(token.LParen)
                new_node = self.parse_sum()
                self.match(token.RParen)
                return new_node
        raise Exception(f"Invalid syntax near {repr(self.current_token)}")

    def match(self, *token_types):
        if type(self.current_token) in token_types:
            last_token = self.current_token
            self.current_token = next(self.tokens)
            print(f"Matched: {last_token}")
            return last_token
        else:
            raise Exception(f"Invalid syntax. Expected {token_types}, but found {type(self.current_token)}")
