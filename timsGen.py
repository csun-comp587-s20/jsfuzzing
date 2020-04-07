# Pull Request #2

class if_statement:
    def __init__(self):
        pass

    def gen(self,bound):
        if bound < 0:
            yield None
        else:
            yield ("(if({}){}else{})".format(expression().gen(bound-1),statement().gen(bound-1),statement().gen(bound-1)))
