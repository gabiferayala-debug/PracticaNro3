def promedio(*numeros):
    resultado = sum(numeros) / len(numeros) if numeros else 0
    print(resultado)

promedio(10, 15, 25, 30)
promedio(10, 15, 25, 30, 50)
promedio()