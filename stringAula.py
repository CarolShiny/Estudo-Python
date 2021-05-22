PALAVRA = "EXEMPLO"
print(PALAVRA[0])
print(PALAVRA[2:5])

print(len(PALAVRA))

nova = PALAVRA + "s!!"
print(nova)

outra = "Novos" + nova
print(outra)

for i in range(len(PALAVRA)):
    print(PALAVRA[i])


lista = [2,4,7]
lista [1] = 9
print(lista)


print("O" in PALAVRA)
print("o" in PALAVRA)
#Eu tbm posso colocar:
print("O" in PALAVRA.lower())

palavra = PALAVRA.lower()
print(palavra)
