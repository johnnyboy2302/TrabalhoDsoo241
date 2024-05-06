class Conta ():
    def __init__(self, codigo_conta: int):
        self.__codigo_conta = codigo_conta
        self.__lista_produtos = []
        self.__pago = False

    @property
    def codigo_conta(self):
        return self.__codigo_conta
    
    @codigo_conta.setter
    def codigo_conta(self, novo):
        if isinstance(novo, int):
            self.__codigo_conta = novo

    @property
    def lista_produtos(self):
        return self.__lista_produtos
    
    @lista_produtos.setter
    def lista_produtos(self, novo):
        if isinstance(novo, list):
            self.__lista_produtos = novo
    
    @property
    def pago(self):
        return self.__pago
    
    @pago.setter
    def pago(self, novo):
        if isinstance(novo, bool):
            self.__pago = novo