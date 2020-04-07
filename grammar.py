# true_false ::= True | False | And(true_false, true_false)
import inspect


class integer:
    def gen(self, bound):
        if bound <= 0:
            yield
        else:
            self.value = [1, 2]
            for each in self.value:
                yield each


class varName:
    def gen(self, bound):
        if bound <= 0:
            yield
        else:
            self.value = ["PETS", "PIES"]
            for each in self.value:
                yield each


class assignment:
    def gen(self, bound):
        if bound <= 0:
            yield
        else:
            for exp in expression().gen(bound - 1):
                for var in varName().gen(bound - 1):
                    yield "{} = {}".format(var, exp)


class expression:
    def gen(self, bound):
        if bound <= 0:
            yield
        else:
            self.value = [expressiondotexpression(), assignment()]
            for each in self.value:
                yield each.gen(bound - 1)

class expressiondotexpression:
    def gen(self, bound):
        if bound <= 0:
            yield
        else:
            for exp1 in varName().gen(bound - 1):
                for exp2 in integer().gen(bound - 1):
                    yield "{}.{}".format(exp1, exp2)

# import random
# class GenerateTerm:
#     def genTerm(self):
#         randInt = random.randint(0, len(self.value)-1)
#         return self.value[randInt]
#
# class cbop:
#     def __init__(self):
#         self.value = ["+", "-", "*", "/", "<<", ">>", ">>>", "&", "|", "^"]
#
# class bop:
#     def __init__(self):
#         self.value = [GenerateTerm.genTerm(cbop()), "<", "<=", ">", "==", "!=", "===", "!==", "&&", "||", "in", ",", "instanceof"]
#
# class n:
#     def __init__(self):
#         self.value = [0, 1]
#
# class b:
#     def __init__(self):
#         self.value = [True, False]
#
# class str:
#     def __init__(self):
#         self.value = ["A", "B"]
#
# class x:
#     def __init__(self):
#         self.value = ["Pets", "Pies"]
#
# class unOp:
#     def __init__(self):
#         self.value = ["void", "typeof", "+", "-", "~", "!"]
#
# class sw:
#     def __init__(self):
#         self.value =["case" + e() + "" + s(), "default" +s()]
#
# class e:
#     def __init__(self):
#         self.value =[
#                         GenerateTerm.genTerm(n()),# integer
#                         GenerateTerm.genTerm(b()), # boolean
#                         GenerateTerm.genTerm(str()), # string
#                        "null", # Null
#                         GenerateTerm.genTerm(x()),  # variable
#                        # x() + "=" + e()
#                        # x() + cbop() + "=" + e() ,
#                        # e()+"" + e()  + "=" +e() ,
#                        # e() + "." + e() +" " + unOp() + "=" + e(),
#                        # e()  + "?" +e() +":" + e(),
#                        # e() + "." + e(),
#                        # "new" + ""+ e() + "(" +")",
#                        # "new" + ""+ e() + "(" + e() + ")",
#                        # e() + "("  + ")",
#                        # e() + "(" + e() + ")",
#                        # "function" + "[" +x() + "]" + "("+ ")" + s() ,
#                        # "function" + "[" +x()+ "]" + "(" + e() +")" + s() ,
#                        # e() + bop() +""+ e() ,
#                        # unOp() +""+  e() ,
#                        # "{" + "}" ,
#                        # "{" + "<"+str() +"," + e()+ ">"+ "}" ,
#                        # "["+ "]",
#                        # "["+ e()+ "]",
#                        # "this",
#                        # "delete" + e(),
#                        # "++" + x(),
#                        # "++" + e()+ "." + e(),
#                        # x() + "++" ,
#                        # e()+ "." + e() + "++" ,
#                        # "--"+ x(),
#                        # "--" + e()+"."+e(),
#                        # x()+"--" ,
#                        # e()+"."+e()+"--" ,
#                        # "eval" + s(),
#         ]

