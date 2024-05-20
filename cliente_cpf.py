from cliente import Cliente

class ClienteCpf(Cliente):

    def __init__(self, nome: str, celular: str, email: str, cpf: str):
        super().__init__(nome, celular, email)
        self.__cpf = cpf
        self.__contas_pagas = []
        self.__quantidade_pratos = 0

    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self, novo):
        self.__cpf = novo

    @property
    def quantidade_pratos(self):
        return self.__quantidade_pratos
    
    @quantidade_pratos.setter
    def quantidade_pratos(self, novo):
        self.quantidade_pratos = novo

    @property
    def conta_ativa(self):
        return self.__conta_ativa

    @conta_ativa.setter
    def conta_ativa(self, nova):
        self.__conta_ativa = nova

    @property
    def contas_pagas(self):
        return self.__contas_pagas
    
    @contas_pagas.setter
    def contas_pagas(self, nova):
        self.contas_pagas = nova