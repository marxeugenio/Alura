import random
nome = input("Informe seu nome: ")
lista = list(range(1000,9999))
token = random.choice(lista)
print(f"O seu nome é {nome} e o seu token é {token}")