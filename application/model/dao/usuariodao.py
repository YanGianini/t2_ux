from application.model.entity.usuario import Usuario

lista_user = []

class UsuarioDao():
    def __init__(self):
        self.lista_user = lista_user

    def getlista_user(self):
        return self.lista_user
