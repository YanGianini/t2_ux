from application.model.entity.ponto import Ponto

class PontoDao():
    def __init__(self) -> None:
        self._lista_ponto = lista_pontos

    def lista_ponto(self):
        return self._lista_ponto


ponto1 = Ponto("centro", "fica no centro ue")
ponto2 = Ponto("Praça nilo peçanha", "Rua 54")
ponto3 = Ponto("Igreja batista", "Rua nossa senhora das graças")
lista_pontos = [ponto1, ponto2, ponto3]