import lexer_token as token

class Lexer:
    def __init__(self):
        pass

    def lex(self, code):
        print(f"=== STARTING LEXING ===")
        tokens = []
        current_token = ""
        for i, character in enumerate(code):
            #print(repr(current_token + character), token.find_token_types(current_token + character))
            token_types = token.find_token_types(current_token + character)
            if not token_types:
                token_type = token.find_token_types(current_token)
                if len(token_type) != 1:
                    raise Exception(f"Unknown token: {repr(current_token)}")
                new_token = token_type[0](current_token)
                tokens.append(new_token)
                if new_token: print(f"New token: {new_token}")
                current_token = character
            else:
                current_token += character

        tokens = list(filter(bool, tokens)) + [token.End]

        print(f"=== FINISHED LEXING ===")
        print()
        return tokens
