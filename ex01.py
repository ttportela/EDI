class Pessoa:
    def __init__(self):
        self.nome = None
        self.idade = None

    def __str__(self):
        return self.nome + ", " + str(self.idade)

# -------------
p = Pessoa()
p.nome = "Chiquinha"
p.idade = 50

q = Pessoa()
q.nome = "Kiko"
q.idade = 48

vetor = [1, 3, 6] 
vetor_pes = [p, q]

print(vetor_pes)