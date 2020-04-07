# Pull Request #2

class if_statement:
    def __init__(self):
        pass

    def gen(self,bound):
        if bound < 0:
            yield None
        else:
            for expr1 in expression().gen(bound -1):
                for stmt1 in statement().gen(bound-1):
                    for stmt2 in statement().gen(bound-1):
                        yield "(if({}){}{})".format(expr1,stmt1, stmt2)
