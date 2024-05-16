from pessoa import Pessoa
from mesa import Mesa
from conta import Conta


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
    
    #essa funcao vai ser ativa sempre no final do dia para dar a comissao pro cara
    def receber_comissao(self):

        comissao_total = 0

        for mesa in self.mesas:
            
            comissao_dessa_mesa = 0

            for conta in self.mesa.contas:

                comissao_dessa_conta = conta.comissao #temos que implementar esse atributo na conta pra facilitar
                comissao_dessa_mesa += comissao_dessa_conta

            comissao_total += comissao_dessa_mesa

        self.comissao = comissao_total 


