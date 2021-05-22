def contaVogais (nome):
    quant = 0
    vogais = ["a","e","i","o","u"]
    for i in range (len(nome)):
        if(nome[i] .lower () in vogais ):
            quant += 1
    return quant        

def procuraS (nome):
    for i in range (len(nome)):
        if (nome[i] == "s"):       
            return True
        else:
            return False
    
def invert (nome):
    novaPalavra = ""
    for i in range (len(nome)):
        novaPalavra = nome[i] + novaPalavra
    return novaPalavra    
