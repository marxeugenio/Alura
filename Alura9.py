import math

numeros = [2, 8, 15, 23, 91, 112, 256]

for numero in numeros:
    raiz = math.sqrt(numero)
    if raiz % 1 == 0:
        print(f"A raiz quadrada de {numero} é um número inteiro: {int(raiz)}")
