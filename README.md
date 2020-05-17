# JSFuzzing

## Grammar 
### Integer 
    n::= 0|1
### Boolean 
    b::= true|false
### String 
    str::= A|B
### Variable 
    x::== Pets| Pies

### Expression 
    e::=  n | b |str | null | x | x = e | e1.e2 = e3 | e1.e2 
### Statement
    s::= e | while e s | if (e) s [s]  
## How to run the generator 

Run the generator by typing the comman below in your choice of shell. The commands accepts one argument: the bound to be used for the grammar. Point to note, the bound is applied to statement. 

     python3 grammar.py [bound]
     Example: python3 grammar.py 3

