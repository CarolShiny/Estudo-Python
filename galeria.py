##import bibGaleriaArte
##quantObras = 4
##valorTotal = 0
##
##for i in range (quantObras):
##    nomeObra= input("Obra:")
##    artista = bibGaleriaArte.consultaArtista (nomeObra)
##    print("Artista: ", artista)
##    if(artista.lower() == "leonardo resende"):
##        preco += bibGaleriaArte.consultaPerco(nomeObra)
##        valorTotal += preco
##
##print ("O valor total das obras é de R$", valorTotal)        


import bibGaleriaArte
quantQuadro= 0
quantEscultura = 0
quantObras = 2

for i in range (quantObras):
    nomeObra= input("Obra:")
    tipo = bibGaleriaArte.consultaTipo (nomeObra)
    
    if(tipo.lower() == "quandro"):
        quantQuadro += 1
        
    elif(tipo.lower() == "escultura"):
        quantEscultura += 1
        
if (quantQuadro > quantEscultura):
    print(quantQuadro)

else:
    print(quantEscultura)
        

 
