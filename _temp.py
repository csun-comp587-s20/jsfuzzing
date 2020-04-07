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
            for exp in expression().gen(bound-1):
                for var in varName().gen(bound-1):
                    yield "{} = {}".format(var, exp)

class expression: 
    def gen(self, bound):
        if bound <= 0:
            yield
        else:
            self.value = [assignment()]
            for each in self.value: 
                yield each.gen(bound-1)



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
                    yield each.gen(bound-1)
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
            for left in true_false().gen(bound-1):
                for right in true_false().gen(bound-1):
                    yield "({} && {})".format(left, right)
    
class bool_or:
    def _init__(self):
        pass
    
    def gen(self, bound): 
        if bound < 0:
            yield None
        else: 
            yield None 
            for left in true_false().gen(bound-1):
                for right in true_false().gen(bound-1):
                    yield "({} || {})".format(left, right)

class bool_not: 
    def _init__(self):
        pass 

    def gen(self, bound): 
        if bound < 0:
            yield None 
        else: 
            yield None
            for component in true_false().gen(bound-1):
                yield component
				
class statement: 
    def gen(self, bound):
        if bound <= 0:
            yield
        else:
            self.value = [expression(), whileStatement()]
			for each in self.value:
				if inspect.isclass(each):
					yield each.gen(bound-1)
					
class whileStatement:
	def gen(self, bound):
		if bound <= 0:
			yield
		else
            yield None  
			for exp in expression().gen(bound-1):
                for stmt in statement().gen(bound-1):
                    yield "(while {} {})".format(exp, stmt)
				
				