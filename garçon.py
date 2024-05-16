from pessoa import Pessoa
from mesa import Mesa


class Garçon(Pessoa):
    def __init__(self, nome: str, celular: str, email: str, cpf: str):
        super().__init__(nome, celular, email)
        self.__cpf = cpf
        self.__comissao = 0.0
        self.__mesas = []

    @property
    def mesas(self):
        return self.__mesas

    def atender_mesa(self, mesa):
        if isinstance(mesa, Mesa) and mesa not in self.mesas:
            self.mesas.append(mesa)

    def rm_mesa(self, mesa):
        if mesa in self.mesa:
            self.mesas.remove(mesa)

    @property
    def comissao(self):
        return self.__comissao
    
    @comissao.setter
    def comissao(self, novo):
        self.__comissao = novo

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo):
        self.__cpf = novo
