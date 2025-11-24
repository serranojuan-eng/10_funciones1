def potencia(base, exponente):
    if exponente<0:
        raise ValueError("Exponente debe ser no negativo")
    resultado=1
    for _ in range(exponente):
        resultado*=base
    return resultado

print(potencia(2,5))
