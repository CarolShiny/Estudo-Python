def criptografa (texto, chave):
    novoTexto = ""
    for i in range(len(texto)):
        codigo = ord(texto[i])
        novoCodigo = codigo + chave
        letra = chr(novoCodigo)
        novoTexto += letra

    return novoTexto


def descriptografa (texto,chave):
    novoTexto = ""
    for i in range(len(texto)):
        codigo = ord(texto[i])
        novoCodigo = codigo - chave
        letra = chr(novoCodigo)
        novoTexto += letra

    return novoTexto
