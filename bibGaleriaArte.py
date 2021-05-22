import random

def consultaPreco (obra):
    return random.randint(2,8) * random.choice([132.40, 275.81, 98.66])

def consultaArtista (obra):
    nome = random.choice(["Manoel", "Dênis", "Adélia", "Patrícia", "Leonardo"])
    sobrenome = random.choice(["Novaes", "Resende", "Gomes", "Lisboa", "Machado"])
    return nome + " " + sobrenome

def consultaQuantObras (artista):
    return random.randint(0,5)

def consultaTipo (obra):
    return random.choice(["Quadro", "Escultura"])
