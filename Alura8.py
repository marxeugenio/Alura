import random
frutas = ["maçã", "banana", "uva", "pêra","manga", "coco", "melancia", "mamão", "laranja", "abacaxi", "kiwi", "ameixa"]

salada_de_frutas = random.sample(frutas,3)

print("salada de frutas surpresa:")
for fruta in salada_de_frutas:
    print(fruta)