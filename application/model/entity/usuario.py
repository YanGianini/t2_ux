class Usuario():
    def __init__(self, nome, email, senha):
        self._nome = nome
        self._email = email
        self._senha = senha

    def get_nome(self):
        return self._nome

    def get_email(self):
        return self._email

    def get_senha(self):
        return self._senha

    def set_nome(self, nome):
        self._nome = nome

    def set_email(self, email):
        self._email = email

    def set_senha(self, senha):
        self._senha = senha