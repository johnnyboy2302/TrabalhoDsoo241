from cliente import Cliente

class ClienteCnpj(Cliente):

    def __init__(self, nome: str, celular: str, email: str, cnpj: str):
        super().__init__(nome, celular, email)
        self.__cnpj = cnpj
        self.__contas_pagas = []
        self.__conta_ativa = None
        self.__desconto = 0.1

    @property
    def desconto(self):
        return self.__desconto
    
    @desconto.setter
    def desconto(self, novo):
        self.desconto = novo

    @property
    def cnpj(self):
        return self.__cnpj
    
    @cnpj.setter
    def cnpj(self, novo):
        self.__cnpj = novo

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