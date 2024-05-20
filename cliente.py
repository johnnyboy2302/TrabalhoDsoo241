from contato import Contato
from pessoa import Pessoa

#é abstrato?
class Cliente(Pessoa):

    def __init__(self, nome: str, celular: str, email: str):
        super().__init__(nome, celular, email)
        self.__contas_pagas = []
        self.__conta_ativa = None

    @property
    def conta_ativa(self):
        return self.__conta_ativa

    @conta_ativa.setter
    def conta_ativa(self, nova):
        self.conta_ativa = nova

    @property
    def contas_pagas(self):
        return self.__contas_pagas
    
    @contas_pagas.setter
    def contas_pagas(self, nova):
        self.contas_pagas = nova