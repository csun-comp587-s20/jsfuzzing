
class s:
    def __init__(self):
        self. value = [
            e(),
            "'\'" + "<{" + s() + "}>",
            "while"+ "(" + e() + "){" + s() + "}",
            "do{"+ s() + "}" + "while(" + e() + ")",
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
            "switch" + e() + "'\'" + "<{" + sw() + "}>", # or s() + w() ? 
        ]
    def eval(self):
        return 'a statement'
            
