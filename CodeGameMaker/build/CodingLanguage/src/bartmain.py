import lexer
import parse

def main():
    content = ""

    with open("test.bart","r") as file:
        content = file.read()

    lex = lexer.Lexer(content)
    tokens = lex.tokenize()

    parser = parse.Parser(tokens)
    parser.parse()

main()