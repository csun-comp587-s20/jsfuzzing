from random import randint

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

# expression
class e:
    def __init__():
        self.value =  [
                       n(), # integer
                       b(), # boolean
                       str(), # string
                       "null", # Null
                       x(),  # variable
                       x() + "=" + e(),
                       x() + cbop() + "=" + e(),
                       e() + e() + "=" e(),
                       e() + "." + e() op() + "=" + e(),
                       e()  + "?" e() +":" + e(),
                       e() + "." + e(),
                       "new" + " "+ e() + "(" +")",
                       "new" + " "+ e() + "(" + e() + ")",
                       e() + "("  + ")",
                       e() + "(" + e() + ")",
                       "function" + "[" +x() + "]" + "("+ ")" + s() ,
                       "function" + "[" +x() + "]" + "(" + e() +")" + s() ,
                       e() + bop() + e() ,
                       unOp() +  e() ,
                       "{" + "}" ,
                       "{" + "<"str() +"," + e()+ ">"+ "}" ,
                       "["+ "]",
                       "["+ e()+ "]",
                       "this",
                       "delete" + e(),
                       "++" + x(),
                       "++" + e()+ "." + e(),
                       x() + "++" ,
                       e()+ "." + e() + "++" ,
                       "--"+ x(),
                       "--" + e()+"."+e(),
                       x()+"--" ,
                       e()+"."+e()+"--" ,
                       "eval" + s(),
                    ]
    def eval():


class s:
    def __init__(self):
        self.value = [
            e(),
            "'\'" + "<{" + s() + "}>",
            "while" + "(" + e() + "){" + s() + "}",
            "do{" + s() + "}" + "while(" + e() + ")",
            "for(" + x() + " in " + s() + ")",
            "for(" + e() + "." + e() + " in " + s() + ")",
            "for(" + s() + ";" + e() + ";" + s() + ";" + ")",
            "var" + x() + "=" + e() + "[," + x() + "=" + e() + "...]",
            "function" + x() + "'\'" + "<{" + x() + "}>" + s(),
            "if(" + e() + ")" + s() + " [" + s() + "]",
            "try([" + x() + s() + "] [" + s() + "])",
            "throw(" + e() + ")",
            "lbl:" + s(),
            "break [" + "lbl" + "]",
            "continue [" + "lbl" + "]",
            "with " + e() + s(),
            "return [" + e() + "]",
            "switch" + e() + "'\'" + "<{" + sw() + "}>",  # or s() + w() ?
        ]

    def eval(self):
        return 'a statement'


