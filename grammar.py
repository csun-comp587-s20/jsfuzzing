class cbop:
    def __init__(self):
        self.value = ["+", "-", "*", "/", "<<", ">>", ">>>", "&", "|", "^"]

class bop:
    def __init__(self):
        self.value = [cbop(), "<", "<=", ">", "==", "!=", "===", "!==", "&&", "||", "in", ",", "instanceof"]
