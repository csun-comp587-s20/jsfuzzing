# true_false ::= True | False | And(true_false, true_false)
import inspect


class integer:
    def __init__(self):
        self.value = [1, 2]

    def gen(self, bound):
        for each in self.value:
            yield each


class varName:
    def __init__(self):
        self.value = ["PETS", "PIES"]

    def gen(self, bound):
        for each in self.value:
            yield each


# eds implementation have class variables represent the inner nodes 4/6/2020
# take a look please ?
class parameterAssignment:
    def __init__(self, e1=None, e2=None, e3=None):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3

    def __str__(self):
        return str(self.e1) + "." + str(self.e2) + " = " + str(self.e3)

    def gen(self, bound):
        for e1 in expression().gen(bound - 1):
            for e2 in expression().gen(bound - 1):
                for e3 in expression().gen(bound - 1):
                    yield parameterAssignment(e1, e2, e3)


# eds implementation of exp
# only produce a leaf node if the bound is 0
# removes the need to check if it is a class or not.

def test():
    for item in expression().gen(2):
        print(item)


class expression:
    def __init__(self):
        self.value = [parameterAssignment()]

    def gen(self, bound):
        if bound <= 0:
            self.value = [integer(), varName()]
            for each in self.value:
                for item in each.gen(0):
                    yield item
        else:
            for each in self.value:
                for item in each.gen(bound-1):
                    yield item





# class expression:
#     def gen(self, bound):
#         if bound <= 0:
#             yield
#         else:
#             self.value = [assignment(), parameterAssignment()]
#             for each in self.value:
#                 yield each.gen(bound - 1)


class true_false:
    def __init__(self):
        pass

    def gen(self, bound):
        if bound < 0:
            yield None
        else:
            yield None
            self.value = ["True", "False", bool_and()]
            for each in self.value:
                if inspect.isclass(each):
                    yield each.gen(bound - 1)
                else:
                    yield each


class bool_and:
    def _init__(self):
        pass

    def gen(self, bound):
        if bound < 0:
            yield None
        else:
            yield None
            for left in true_false().gen(bound - 1):
                for right in true_false().gen(bound - 1):
                    yield "({} && {})".format(left, right)


class bool_or:
    def _init__(self):
        pass

    def gen(self, bound):
        if bound < 0:
            yield None
        else:
            yield None
            for left in true_false().gen(bound - 1):
                for right in true_false().gen(bound - 1):
                    yield "({} || {})".format(left, right)


class bool_not:
    def _init__(self):
        pass

    def gen(self, bound):
        if bound < 0:
            yield None
        else:
            yield None
            for component in true_false().gen(bound - 1):
                yield component

# ed similar to group coding
# class parameterAssignment:
#     def gen(self, bound):
#         if bound <= 0:
#             yield
#         else:
#             for e1 in expression().gen(bound - 1):
#                 for e2 in expression().gen(bound - 1):
#                     for e3 in expression().gen(bound - 1):
#                         yield "{}.{} = {}".format(e1, e2, e3)


# class assignment:
#     def gen(self, bound):
#         if bound <= 0:
#             yield
#         else:
#             for exp in expression().gen(bound - 1):
#                 for var in varName().gen(bound - 1):
#                     yield "{} = {}".format(var, exp)
