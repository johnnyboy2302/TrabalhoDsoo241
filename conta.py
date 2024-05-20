class Conta ():
    def __init__(self, codigo: int):
        self.__codigo_conta = codigo
        self.__produtos = []
        self.__pago = False
        self.__comissao = 0.0

    @property
    def codigo_conta(self):
        return self.__codigo_conta
    
    @codigo_conta.setter
    def codigo(self, novo):
        if isinstance(novo, int):
            self.__codigo_conta = novo

    @property
    def comissao(self):
        return self.__comissao
    
    @comissao.setter
    def comissao(self, novo):
        self.comissao = novo

    @property
    def produtos(self):
        return self.__produtos
    
    #cara eu acho que deveria ter um incluir e excluir e nao um setter direto
    @produtos.setter
    def produtos(self, novo):
        if isinstance(novo, list):
            self.__produtos = novo
    
    @property
    def pago(self):
        return self.__pago
    
    @pago.setter
    def pago(self, novo):
        if isinstance(novo, bool):
            self.__pago = novo

    def valor_total(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.preco
        return soma
    
    def despesa_total(self):
        soma = 0 
        for produto in self.produtos:
            soma += produto.despesa
        return soma
    
