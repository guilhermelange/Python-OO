class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes}'


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} - {self.duracao}'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} - {self.temporadas}'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    #herda o for in, in e [0]
    def __getitem__(self, item):
        self._programas[item]

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
filme2 = Filme('Todo Mundo em Pânico', 1999, 100)
serie2 = Serie('Demolidor', 2006, 2)


filme2.dar_like()
filme2.dar_like()
serie2.dar_like()
serie2.dar_like()
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, serie2, filme2]
play_fim_de_semana = Playlist('Fim de Semana', filmes_e_series)

print(f'A Playlist possui {len(play_fim_de_semana)} filmes')

for programa in play_fim_de_semana.listagem:
    print(programa)

#print(serie2 in play_fim_de_semana)