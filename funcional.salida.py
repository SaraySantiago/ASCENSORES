def sumar(a,b):
    return a+b

def multiplicar(a,b):
    return a*b

def elige():
    print ("sumar 1")
    print ("multiplicar 2")
    op = input ("que quieres")
    if op == "1": 
        return sumar 
    if op == "2":
        return multiplicar
    
Opera = elige ()
print (Opera(2,3))