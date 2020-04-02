class cbop:
    def __init__(self):
        self.value = ["+", "-", "*", "/", "<<", ">>", ">>>", "&", "|", "^"]

class bop:
    def __init__(self):
        self.value = [cbop(), "<", "<=", ">", "==", "!=", "===", "!==", "&&", "||", "in", ",", "instanceof"]

class Integer:
    def __init__(self):
        self.value = [0, 1]

class Boolean:
    def __init__(self):
        self.value = [true, false]
        
class String:
    def __init__(self):
        self.value = ["A", "B"]

class Variable: 
    def __init__(self):
        self.value = ["Pets", "Pies"]