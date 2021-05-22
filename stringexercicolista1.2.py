import stringExercicio
#questôes de 2 a 5: programa

palavra = input("Digite uma palavra:")

resultado = stringExercicio.contaVogais(palavra)
print(resultado)

letraS = stringExercicio.procuraS(palavra)
print(letraS)

PalavraInvertida = stringExercicio.invert(palavra)
print(PalavraInvertida)
