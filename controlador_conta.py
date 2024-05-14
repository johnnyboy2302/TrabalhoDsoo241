from tela_conta import TelaConta
class ControladorConta():
    def __init__(self):
        self.__tela_conta = TelaConta()
        self.__contas = []

    @property
    def tela_conta(self):
        return self.__tela_conta
    
    @property
    def contas(self):
        return self.__contas
    
    def adiciona_conta(self):
        conta_dados = self.tela_conta.pega_dados_conta()

    #aqui eu acho que da pra aceitar pedido repetido, desde que nao seja o mesmo codigo
    #a pessoa pode pedir dois refris iguais 
    def adiciona_produto(self):
        self.lista_contas()    
        self.escolhe_conta()
    
    """ def remove_produto(self):

    #aqui eu penso que temos que listar as contas e pedidos
    def lista_contas(self):

    def escolhe_conta(self):

    def pagar_conta(self): 


    #aqui vamos automatizar do jeito que tu falou
    #tu acha melhor numeros aleatorios ou uma ordem?
    def criar_conta(self):
    
"""