from tela_conta import TelaConta


class ControladorConta():
    def __init__(self):
        self.__tela_conta = TelaConta()
        self.__contas_pagas = []
        self.__contas = []

    @property
    def tela_conta(self):
        return self.__tela_conta
    
    @property
    def contas(self):
        return self.__contas
    
    @property
    def contas_pagas(self):
        return self.__contas_pagas
    
    def criar_conta(self):
        pass

    def adiciona_produto(self):
        self.lista_contas()    
        self.escolhe_conta()
    
    def remover_produto(self):
        pass

    def lista_contas(self):
        pass

    def pagar_conta(self):
        pass

    def adicionar_produto(self):
        pass

    def listar_produtos_de_uma_conta(self):
        pass

    def mostrar_contas(self):
        pass

    def mostrar_contas_pagas(self):
        pass

    def deletar_conta(self):
        pass

    def criar_conta(self):
        pass

    #status: feito
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op = int(self.tela_conta.tela_opcoes())
            except:
                self.tela_conta.mostra_msg("opção não é um inteiro")
                op = None
            if op == 1:
                self.criar_conta()
            elif op == 2:
                self.adicionar_produto()
            elif op == 3:
                self.remover_produto()
            elif op == 4:
                self.listar_produtos_de_uma_conta()
            elif op == 5:
                self.pagar_conta()
            elif op == 6:
                self.mostrar_contas()
            elif op == 7:
                self.mostrar_contas_pagas()
            elif op == 8:
                self.deletar_conta()
            elif op == 0:
                continua = False
            else: 
                self.tela_contato.mostra_msg("opção inválida")