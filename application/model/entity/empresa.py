class Empresa():
    def __init__(self, email, senha, CNPJ):
        self._email = email
        self._senha = senha
        self._cnpj = CNPJ

    def get_email(self):
        return self._email

    def get_senha(self):
        return self._senha

    def get_cnpj(self):
        return self._cnpj

    def set_email(self, email):
        self._email = email

    def set_senha(self, senha):
        self._senha = senha

    def set_cnpj(self, cnpj):
        self.cnpj = cnpj