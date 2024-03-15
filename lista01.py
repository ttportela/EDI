# Estrutura:
class Node: # Nó, Elemento
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None

class Lista:
    def __init__(self):
        self.primeiro = None

    def imprimir(self):
        aux = self.primeiro
        while aux != None:
            print(aux.nome)
            aux = aux.proximo

    def add(self, nome):
        novo = Node(nome)
        if self.primeiro == None:
            self.primeiro = novo
        else:
            aux = self.primeiro
            while aux.proximo != None:
                aux = aux.proximo
            aux.proximo = novo


# Programa:
# 💥💥💥 Prepare to have your mind blown 💥💥💥
l = Lista()
l.add("Pedro Cava.")
l.add("Pedro V.")
l.add("Willian B.")

l.imprimir()

