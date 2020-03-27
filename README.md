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
### Uni-Operation
    unOp:== void | typeof | + | - | ~ | !
### Compound Bin Operation
    cbop:== + | - | * | / | << | >>| >>> | & | `|` | ^
### Bin Operation 
    bop::= cbop | < | <= | > | >= | == | != | === | !== | && | || | in | , | instanceof
### Label 
    lbl::= 'turtle' | 'dove'
### Switch Component 
    sw::=  case e s | default s
### Expression 
    e::=  n | b |str | null | x | x = e | x cbop = e | e1.e2 = e3 | e1.e2 op = e3 
    |  e1 ? e2 : e3 | e1.e2 | new e1(\vec{e2}) | e1(\vec{e2}) | function [x](\vec{x}) s 
    | e1 bop e2 | unOp e | \{ \vec{<str, e>} \ | [\vec{e}] | this| delete e | ++x 
    | ++e1.e2 | x++ | e1.e2++ | --x | --e1.e2| x-- | e1.e2-- | eval S 

### Statement
    s::= e | \vec{s} | while e s | do s while e | for x in s | for e.e in s 
    | for(s;e;s) s | var x = e[,x = e...] | function x(\vec{x}) s | if (e) s [s] 
    | trys [x s] [s] | throw e | lbl: s | break [lbl] | continue [lbl] | with e s 
    | return [e] | switch e \vec{sw}

