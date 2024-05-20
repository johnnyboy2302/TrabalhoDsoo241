

class Mesa():

    def __init__(self, numero_da_mesa, controlador_conta):
        self.__garçon = None
        self.__numero_da_mesa = numero_da_mesa
        self.__contas = []
        self.__controlador_conta = controlador_conta

    @property
    def controlador_conta(self):
        return self.__controlador_conta
    
    @property
    def garçon(self):
        return self.__garçon
    
    @garçon.setter
    def garçon(self, novo):
        self.__garçon = novo

    @property
    def numero_da_mesa(self):
        return self.__numero_da_mesa
    
    @numero_da_mesa.setter
    def numero_da_mesa(self, novo):
        self.numero_da_mesa = novo

    @property
    def contas(self):
        return self.__contas
    
    @contas.setter
    def contas(self, nova):
        self.contas = nova