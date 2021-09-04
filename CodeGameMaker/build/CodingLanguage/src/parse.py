from Objects.varObject import VariableObject

class Parser(object):
    def __init__(self,tokens):
        self.tokens = tokens
        self.token_index = 0
        self.tranpiled_code = ""

    def parse(self):
        while self.token_index < len(self.tokens):
            token_type = self.tokens[self.token_index][0]
            token_value = self.tokens[self.token_index][1]

            if token_type == "VAR_DECLERATION" and token_value == "var":
                self.parse_varible_decleration(self.tokens[self.token_index:len(self.tokens)])

            self.token_index += 1
        print(self.tranpiled_code)

    def parse_varible_decleration(self, token_stream):
        tokens_checked = 0

        name = ""
        operator = ""
        value = ""

        for token in range(0,len(token_stream)):
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]
            
            if token == 4 and token_type == "STATMENT_END": break

            elif token == 1 and token_type == "IDENTIFIER":
                name = token_value
            elif token == 1 and token_type != "IDENTIFIER":
                print("ERROR: INVALID VARIBLE NAME '"+token_value+"'")
                quit()

            elif token == 2 and token_type == "OPERATOR":
                operator = token_value

            elif token == 1 and token_type != "OPERATOR":
                print("ERROR: Assigment Operator is missing or invalid it should be '='")
                quit()

            elif token == 3 and token_type in ["STRING","INTEGER","IDENTIFIER"]:
                value = token_value
            elif token == 3 and token_type not in ["STRING","INTEGER","IDENTIFIER"]:
                print("INVALID Varible Assigment Value'"+token_value+"'")
                quit()
            
            tokens_checked += 1

        varObj = VariableObject()
        self.tranpiled_code += varObj.transpile(name,operator,value)
        
        self.token_index = tokens_checked