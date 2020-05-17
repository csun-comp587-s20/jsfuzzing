import sys 
import random

def random_fail():
    return False

class integer:
    def __init__(self):
        self.value = [0, 1]

    def gen(self, bound=None):
        for each in self.value:
            yield each


class boolean:
    def __init__(self):
        self.value = [True, False]

    def gen(self, bound=None):
        for each in self.value:
            yield each


class varName:
    def __init__(self):
        self.value = ["PETS", "PIES"]

    def gen(self, bound=None):
        for each in self.value:
            yield each


class string:
    def __init__(self):
        self.value = ["A", "B"]

    def gen(self, bound=None):
        for each in self.value:
            yield each


class BaseExpression:
    def __init__(self, value=None):
        self.value = [integer(), varName(), boolean(), string(),
                      ExpAssignment(), Exp1DotExp2EqualsExp(), Exp1DotExp2()]

    def gen(self, bound):
        if bound <= 0 or random_fail():
            for each in self.value:
                for item in each.gen(0):
                    yield item
        else:
            for each in self.value:
                for item in each.gen(bound-1):
                    yield item


class ExpAssignment:
    def __init__(self, v1=None, e1=None):
        self.e1 = e1
        self.v1 = v1

    def __str__(self):
        return str(self.v1) + "=" + str(self.e1)

    def gen(self, bound):
        if bound <= 0  or random_fail():
            pass
        else:
            for v1 in varName().gen():
                for e1 in BaseExpression().gen(bound-1):
                    yield ExpAssignment(e1, v1)


class Exp1DotExp2EqualsExp:
    def __init__(self, e1=None, e2=None, e3=None):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3

    def __str__(self):
        return str(self.e1) + "[" + str(self.e2)  + "]"+ "=" + str(self.e3)

    def gen(self, bound):
        if bound <= 0  or random_fail():
            pass
        else:
            for e1 in BaseExpression().gen(bound-1):
                for e2 in BaseExpression().gen(bound-1):
                    for e3 in BaseExpression().gen(bound-1):
                        yield Exp1DotExp2EqualsExp(e1, e2, e3)


class Exp1DotExp2:
    def __init__(self, e1=None, e2=None):
        self.e1 = e1
        self.e2 = e2

    def __str__(self):
        return str(self.e1) + "[" + str(self.e2) + "]"

    def gen(self, bound):
        if bound <= 0  or random_fail():
            pass
        else:
            for e1 in BaseExpression().gen(bound-1):
                for e2 in BaseExpression().gen(bound-1):
                    yield Exp1DotExp2(e1, e2)


class statement:
    def __init__(self, value=None):
        self.value = [BaseExpression(), ifStatement(), whileStatement()]

    def gen(self, bound):
        if bound <= 0  or random_fail():
            for each in self.value:
                for item in each.gen(0):
                    yield item
        else:
            for each in self.value:
                for item in each.gen(bound-1):
                    yield item


class ifStatement:
    def __init__(self, e1=None, stmt1=None, stmt2=None):
        self.e1 = e1
        self.stmt1 = stmt1
        self.stmt2 = stmt2

    def __str__(self):
        return "if(" + str(self.e1) + ") " + str(self.stmt1) + " " + str(self.stmt2)

    def gen(self, bound):
        if bound <= 0  or random_fail():
            pass
        else:
            for e1 in BaseExpression().gen(bound-1):
                for stmt1 in statement().gen(bound-1):
                    for stmt2 in statement().gen(bound-1):
                        yield ifStatement(e1, stmt1, stmt2)


class whileStatement:
    def __init__(self, e1=None, stmt1=None):
        self.e1 = e1
        self.stmt1 = stmt1

    def __str__(self):
        return "while " + str(self.e1) + " " + str(self.stmt1)

    def gen(self, bound):
        if bound <= 0  or random_fail():
            pass
        else:
            for e1 in BaseExpression().gen(bound-1):
                for stmt1 in statement().gen(bound-1):
                    yield whileStatement(e1, stmt1)


def entry_point(bound):
    generationObject = statement()
    generator = generationObject.gen(bound)
    f = open("test.txt", "w")
    for item in generator:
        f.write(str(item)+ "\n")
    f.close()


if __name__ == "__main__":
    if (len(sys.argv) <= 1):
        print("Error: bound not found. \nPlease enter the bound as grammar.py [bound]")
    else: 
        bound = int(sys.argv[1])
        entry_point(bound)
