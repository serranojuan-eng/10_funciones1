def invertir(cadena):
    if cadena=="":
        return ""
    return invertir(cadena[1:]) + cadena[0]

def es_palindromo(cadena):
    return cadena == invertir(cadena)

print(es_palindromo("ana"))
