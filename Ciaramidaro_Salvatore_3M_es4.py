import random

def numero_casuale():
    return random.randint(0, 99)

def descrizione_casuale():
    nomi = ["Pippo", "Pluto", "Paperino", "Topolino", "Minnie"]
    nome = random.choice(nomi)
    eta = numero_casuale()
    return "{} ha {} anni.".format(nome, eta)
    print(descrizione_casuale())
"Pluto ha 23 anni."

