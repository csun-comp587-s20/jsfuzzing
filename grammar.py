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

class expression:
    def __init__(self):
        self.value = [expressiondotexpression()]

    def gen(self, bound):
        if bound <= 0:
            self.value = [integer(), varName()]
            for each in self.value:
                for item in each.gen(0):
                    yield item
        else:
            for each in self.value:
                for item in each.gen(bound -1):
                    yield item

class expressiondotexpression:
    def __init__(self, e1, e2):
            self.e1 = e1
            self.e2 = e2

    def __str__(self):
        return str(self.e1) + "." + str(self.e2)

    def gen(self, bound):
        for e1 in expression().gen(bound -1):
            for e2 in expression().gen(bound-1):
                yield expressiondotexpression(e1, e2)

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
        return str("if(" +e1 +") " +stmt1 + " " + stmt2)

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
        return str("while " +e1 +" " +stmt1 +)

    def gen(self,bound):
        for e1 in expression().gen(bound -1):
            for stmt1 in statement().gen(bound-1):
                    yield whileStatement(e1, stmt1)