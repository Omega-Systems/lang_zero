import lexer_token as token

class Lexer:
    def __init__(self):
        pass

    def lex(self, code):
        print(f"=== STARTING LEXING ===")
        tokens = []
        current_token = ""
        for character in code:
            #print(repr(current_token + character), token.find_token_types(current_token + character))
            token_types = token.find_token_types(current_token + character)
            if token_types:
                current_token += character
            else:
                possible_token_types = token.find_token_types(current_token)
                if len(possible_token_types) == 1:
                    new_token = possible_token_types[0](current_token)
                    tokens.append(new_token)
                    if new_token: print(f"New token: {new_token}")
                    current_token = character

        if current_token != " ":
            raise Exception(f"Unknown token: {repr(current_token)}")


        tokens = list(filter(bool, tokens)) + [token.End]

        print(f"=== FINISHED LEXING ===")
        print()
        return tokens
