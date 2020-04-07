# JSFuzzing

## Grammar 
### Integer 
    n::= 0|1
### Boolean 
    b::= true|false
### String 
    str::= A|B
### Variable 
    x:== Pets| Pies

### Expression 
    e::=  n | b |str | null | x | x = e | e1.e2 = e3 | e1.e2 
### Statement
    s::= e | while e s | if (e) s [s] 

