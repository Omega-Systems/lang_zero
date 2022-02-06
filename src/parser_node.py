class Node(object):
    pass

class BinaryOp(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.left}) {self.op} ({self.right})"

    def output(self, depth=0):
        print(f"{'    ' * depth}{self.op}")
        self.left.output(depth + 1)
        self.right.output(depth + 1)

class UnaryOp(Node):
    def __init__(self, op, arg):
        self.op = op
        self.arg = arg

    def __str__(self):
        return f"{self.op} ({self.arg})"

    def output(self, depth=0):
        print(f"{'    ' * depth}{self.op}")
        self.arg.output(depth + 1)

class Integer(Node):
    def __init__(self, value):
        self.value: int = value.value

    def __str__(self):
        return f"{self.value}"

    def output(self, depth=0):
        print(f"{'    ' * depth}{self.value}")

class Identifier(Node):
    def __init__(self, value):
        self.value: str = value.value

    def __str__(self):
        return f"{self.value}"

    def output(self, depth=0):
        print(f"{'    ' * depth}{self.value}")

class VarDeclaration(Node):
    def __init__(self, variable, value):
        self.variable = variable
        self.value = value

    def __str__(self):
        return f"{name}: {datatype} = value"

    def output(self, depth=0):
        print(f"{'    ' * depth}{self.variable}")
        self.value.output(depth + 1)

class Compound(Node):
    def __init__(self, statement_list):
        self.statement_list = statement_list

    def __str__(self):
        return f""

    def output(self, depth=0):
        print(f"{'    ' * depth}COMPOUND")
        for statement in self.statement_list:
            statement.output(depth + 1)

class Function(Node):
    def __init__(self, name, arguments, return_type, body):
        self.name = name
        self.arguments = arguments
        self.return_type = return_type
        self.body = body

    def __str__(self):
        return f""

    def output(self, depth=0):
        print(f"{'    ' * depth}FUNCTION {self.name}: {self.return_type}")
        print(f"{'    ' * (depth + 1)}ARGUMENTS")
        for argument in self.arguments:
            argument.output(depth + 2)
        self.body.output(depth + 1)

class Variable(Node):
    def __init__(self, name, datatype):
        self.name = name
        self.datatype = datatype

    def __str__(self):
        return f"VARIABLE {self.name}: {self.datatype}"

    def output(self, depth=0):
        print(f"{'    ' * depth}VARIABLE {self.name}: {self.datatype}")

class Return(Node):
    def __init__(self, value):
        self.value = value

    def output(self, depth=0):
        print(f"{'    ' * depth}RETURN")
        self.value.output(depth + 1)
