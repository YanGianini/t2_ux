class Ponto():
    def __init__(self, nome, localizacao):
        self._nome = nome
        self._localizacao = localizacao

    def get_nome(self):
        return self._nome

    def get_localizacao(self):
        return self._localizacao

    def set_nome(self, nome):
        self._nome = nome

    def set_localizacao(self, localizacao):
        self._localizacao = localizacao

