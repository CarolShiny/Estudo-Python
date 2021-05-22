import bibListas
##numeros = [-40,-8,-5,-9]
##resultado = bibListas.somaLista(numeros)
##
##print("o resultado da soma é", resultado)
##
##for i in numeros:
##    resultado = bibListas.maiorLista(numeros)
##
##print("O maior número é", resultado[-1])

Idade = []

quant = int(input("Quantas idades vai colocar?"))

for i in range (quant):
    idades = int(input("Digite uma idade:"))
    Idade.append(idades)

resultado = bibListas.somaLista(Idade)

media = resultado / quant

print(media)

    

    
    

