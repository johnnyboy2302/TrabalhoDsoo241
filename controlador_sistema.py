from tela_sistema import TelaSistema
from controlador_produto import ControladorProduto
from controlador_conta import ControladorConta

class ControladorSistema:

    def __init__(self):
        self.__controlador_produto = ControladorProduto()
        self.__controlador_conta = ControladorConta()
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_produto(self):
        return self.__controlador_produto

    @property
    def controlador_conta(self):
        return self.__controlador_conta

    def cadastra_produtos(self):
        # Chama o controlador de produtos
        self.__controlador_produto.abre_tela()

    def cadastra_contas(self):
        # Chama o controlador de Amigos
        self.__controlador_conta.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op = int(self.__tela_sistema.tela_opcoes())

            except:
                self.__tela_sistema.mostra_msg("Esta opção não é um inteiro")
                op = None
            
            if op == 1:
                self.controlador_produto.abre_tela_inicial()
            
            elif op == 2:
                self.controlador_conta.abre_tela_inicial()
            
            elif op == 0:
                continua = False

            else:
                self.tela_produtos.mostra_msg("Opção inválida")
