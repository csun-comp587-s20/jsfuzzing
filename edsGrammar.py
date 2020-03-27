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

