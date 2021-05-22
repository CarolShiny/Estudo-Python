import random
import time
inicio = str.lower(input("Deseja Iniciar o jogo? "))
while(inicio == "sim"):
    print("Let's go!")
    modo = (input('''Selecione um modo que deseja jogar:
[Fácil]
[Médio]
[Difícil]
Qual é a sua opção?''')) . lower()
    if(modo == "facil"):
        quantCoresSenha = 3
        tentativas = 10
        listaCores = ["vermelho", "azul", "verde", "amarelo"]
    elif (modo == "medio"):
        quantCoresSenha = 4
        tentativas = 20
        listaCores = ["vermelho", "azul", "verde", "amarelo", "laranja"]
    elif (modo == "dificil"):
        quantCoresSenha = 5
        tentativas = 30
        listaCores = ["vermelho", "azul", "verde", "amarelo", "laranja", "roxo"]
    listaSenha = []
    listaJogador = []
    posicaoCerta = 0
    corCerta = 0
    
    print("Essas são as cores que você pode ultilizar: {}".format(listaCores))
    for i in range(quantCoresSenha):
        senha = random.choice(listaCores)
        listaSenha.append(senha)
    ##print("Senha = {}".format(listaSenha))
    while(tentativas != 0):
        for i in range (quantCoresSenha):
            escolhaJogador = str.lower(input("Digite uma cor: "))
            listaJogador.append(escolhaJogador)
        if (listaJogador[0] == listaSenha[0]) and (listaJogador[1] == listaSenha[1]) and (listaJogador[2] == listaSenha[2]):  
            print("Parabéns você conseguiu acerta a sequência!!")
            tentativa = 0
        else:
            for i in range(quantCoresSenha):
                if listaJogador[i] in listaSenha:
                    corCerta += 1                
            for i in range(quantCoresSenha):
                if listaJogador[i] == listaSenha[i] :
                    posicaoCerta += 1        
            print("Infelizmente você não conseguiu!! VOCÊS AINDA TEM {} CHANCES".format(tentativas - 1))
            print("Na sua tentativa você acertou {} cores e {} posições".format(corCerta, posicaoCerta))       
            listaJogador = []
            corCerta = 0
            posicaoCerta = 0
            tentativas = tentativas - 1
    inicio = str.lower(input("Deseja jogar novamente? "))
if(inicio != "sim"):
    print("Finalizando...")
    time.sleep(3)
    print("Obrigado por jogar.Te esperamos novamente em breve!! ")
