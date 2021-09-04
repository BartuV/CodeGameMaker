import re

class Lexer:
    def __init__(self,code):
        self.code = code

    def tokenize(self):
        tokens = []

        #burada kelimelere ayırıyoruz
        code = self.code.split()

        #burada sözcüklerin indexini ayarlıyoruz
        source_index = 0

        #burada bütün dosyayı inceliyoruz
        while source_index < len(code):
            word = code[source_index]

            if word == 'var' : tokens.append(["VAR_DECLERATION", word])
            elif re.match("[a-z]",word) or re.match("[A-Z]",word):
                if word[len(word)-1] == ";":
                    tokens.append(["IDENTIFIER",word[0:len(word) - 1]])
                else:
                    tokens.append(["IDENTIFIER", word])
            elif re.match("[0-9]",word):
                if word[len(word)-1] == ";":
                    tokens.append(["INTEGER",word[0:len(word) - 1]])
                else:
                    tokens.append(["INTEGER",word])
            elif word in "=/*=-+":
                tokens.append(["OPERATOR",word])
            if word[len(word)-1] == ";":
                tokens.append(["STATMENT_END", ";"])
            source_index += 1
        print(tokens)
        return tokens