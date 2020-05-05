import inspect


class integer:
    def __init__(self):
        self.value = [0,1]

    def gen(self):
        for each in self.value:
            yield each

class boolean:
    def __init__(self):
        self.value = [True, False]

    def gen(self):
        for each in self.value:
            yield each

class varName:
    def __init__(self):
        self.value =["PETS", "PIES"]

    def gen(self):
        for each in self.value:
            yield each

class string:
    def __init__(self):
        self.value =["A", "B"]

    def gen(self):
        for each in self.value:
            yield each

class expression:
    def __init__(self):
        self.value = [ExpAssignment(), Exp1DotExp2EqualsExp(), Exp1DotExp2()]

    def gen(self, bound):
        if bound <= 0:
            self.value = [integer(), varName(), boolean(), string(), None]
            for each in self.value:
                for item in each.gen(0):
                    yield item
        else:
            for each in self.value:
                for item in each.gen(bound -1):
                    yield item

class ExpAssignment:
    def __init__(self, v1, e1):
            self.e1 = e1
            self.v1 = v1

    def __str__(self):
        return  str(self.v1)+ "=" + str(self.e1)

    def gen(self, bound):
        for v1 in varName().gen(bound -1):
            for e1 in expression().gen(bound -1):
                 yield ExpAssignment(e1, v1)

class Exp1DotExp2EqualsExp:
    def __init__(self, e1, e2, e3):
            self.e1 = e1
            self.e2 = e2
            self.e3 = e3
    def __str__(self):
        return str(self.e1) + "." + str(self.e2) + "=" + str(self.e3)

    def gen(self, bound):
        for e1 in expression().gen(bound -1):
            for e2 in expression().gen(bound-1):
                for e3 in expression().gen(bound-1):
                    yield Exp1DotExp2EqualsExp(e1, e2, e3)

class Exp1DotExp2:
    def __init__(self, e1, e2):
            self.e1 = e1
            self.e2 = e2

    def __str__(self):
        return str(self.e1) + "." + str(self.e2)

    def gen(self, bound):
        for e1 in expression().gen(bound -1):
            for e2 in expression().gen(bound-1):
                yield Exp1DotExp2(e1, e2)

class statement:
    def gen(self, bound):
        if bound <= 0:
            self.value = [ifStatement(), whileStatement(), expression()]
            for each in self.value:
                for item in each.gen(0):
                    yield item
        else:
            for each in self.value:
                for item in each.gen(bound -1):
                    yield item

class ifStatement:
    def __init__(self, e1, stmt1, stmt2):
        self.e1 = e1
        self.stmt1 = stmt1
        self.stmt2 = stmt2

    def __str__(self):
        return "if(" +str(self.e1) +") " +str(self.stmt1) + " " + str(self.stmt2)

    def gen(self,bound):
        for e1 in expression().gen(bound -1):
            for stmt1 in statement().gen(bound-1):
                for stmt2 in statement().gen(bound-1):
                    yield ifStatement(e1, stmt1, stmt2)

class whileStatement:
    def __init__(self, e1, stmt1):
        self.e1 = e1
        self.stmt1 = stmt1

    def __str__(self):
        return "while " +str(self.e1) +" " +str(self.stmt1)

    def gen(self,bound):
        for e1 in expression().gen(bound -1):
            for stmt1 in statement().gen(bound-1):
                    yield whileStatement(e1, stmt1)