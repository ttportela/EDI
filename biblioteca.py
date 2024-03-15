class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.numExemplares = 0
    
    def imprimir(self):
        print("   >", self.titulo, '-', self.autor)

class Usuario:
    def __init__(self, nome, ra):
        self.nome = nome
        self.ra = ra

class Emprestimo:
    def __init__(self, data, usuario: Usuario):
        self.data = data
        self.usuario = usuario
        self.livros = []
    
    def imprimir(self):
        print("Empréstimo:")
        print("- Data:", self.data)
        print("- Usuário:", self.usuario.nome)
        print("- Livros: -")
        for livro in self.livros:
            livro.imprimir()


# --------------------------
l1 = Livro("Sistemas Telefônicos Fixos e Móveis", "Tarlis Portela")
l1.numExemplares = 10
l2 = Livro("Estruturas de Dados", "Cormen")
l3 = Livro("Pequeno Manual Antiracista", "Djamila Ribeiro")
l2.numExemplares = 5
l3.numExemplares = 20

u1 = Usuario("Jorge Amado", 2344532)
u2 = Usuario("Joseph Climber", 123532)

# ---------------------------------
e1 = Emprestimo('2024-03-08', u2)
e1.livros.append(l1)
e1.livros.append(l2)

e2 = Emprestimo('2024-03-05', u1)
e2.livros.append(l2)
e2.livros.append(l3)

emprestimos = [e1, e2]

e2.usuario = u2

for e in emprestimos:
    e.imprimir()
    print('--------------------------')
