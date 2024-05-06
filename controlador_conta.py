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
    

