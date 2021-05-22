##palavra = "Segredo"
##novaPalavra = ""
##for i in range(len(palavra)):
##    codigo = ord(palavra[i])
##    novoCodigo = codigo + 5
##    letra = chr(novoCodigo)
##    novaPalavra += letra
##print(novaPalavra)


import bibCriptografia

mensagem = input("Qual a mensagem a ser criptografada?")
numero = int(input("Indique um valor para ser a chave de criptografia:"))
novaMensagem = bibCriptografia.criptografa(mensagem,numero)
    
print("Mensagem criptografada")
print(novaMensagem)


descript = bibCriptografia.descriptografa(mensagem,numero)
print(descript)
