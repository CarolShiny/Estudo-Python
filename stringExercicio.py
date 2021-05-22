def quantPontuacao (texto):
    quant = 0
    pontuacao = [".",",","?","!",":",";"]
    for i in range (len(texto)):
        if(texto[i] in pontuacao):
            quant += 1

    return quant        
            
