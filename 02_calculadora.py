def sumar(a,b): return a+b
def restar(a,b): return a-b
def multiplicar(a,b): return a*b
def dividir(a,b):
    if b==0: raise ZeroDivisionError("No dividir entre cero")
    return a/b

def calculadora():
    op=input("Operación (+,-,*,/): ")
    a=float(input("A: "))
    b=float(input("B: "))
    if op=="+": print(sumar(a,b))
    elif op=="-": print(restar(a,b))
    elif op=="*": print(multiplicar(a,b))
    elif op=="/": print(dividir(a,b))
    else: print("Operación inválida")

if __name__=="__main__":
    calculadora()
