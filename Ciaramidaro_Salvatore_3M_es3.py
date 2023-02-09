import random

def numero_casuale():
    return random.randint(0, 99)

def descrizione_eta_casuale(nome):
    eta = numero_casuale()
    return "{} ha {} anni.".format(nome, eta)
print(descrizione_eta_casuale("Pippo"))
"Pippo ha 23 anni."








