def contar_digitos(n):
    n=abs(n)
    if n==0: return 1
    c=0
    while n>0:
        c+=1
        n//=10
    return c

print(contar_digitos(12345))
