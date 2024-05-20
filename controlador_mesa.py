from tela_mesa import TelaMesa
from mesa import Mesa
from controlador_conta import ControladorConta

class ControladorMesa():

    def __init__(self, controlador_sistema):
        self.__tela_mesa = TelaMesa()
        self.__controlador_sistema = controlador_sistema
        self.__mesas = []

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def mesas(self):
        return self.__mesas

    @property
    def tela_mesa(self):
        return self.__tela_mesa
    
    def contas_pagas(self, mesa):
        return mesa.controlador_conta.contas_pagas

    #status: feito, testar   
    def criar_mesa(self) -> bool:
        num_mesas = len(self.mesas)

        nova_mesa = Mesa(num_mesas + 1, ControladorConta(self.controlador_sistema))

        self.mesas.append(nova_mesa)

    
    #status: fazer    
    def excluir_mesa(self):
        mesa = self.acha_mesa_by_num()

        if mesa in self.mesas:
            self.mesas.remove(mesa)
            self.tela_mesa.mostra_msg('Mesa excluída')
        else:
            self.tela_mesa.mostra_msg("Atenção: Mesa inexistente")


    #status: incompleta  
    def listar_mesa(self):
        for mesa in self.mesas:
            self.tela_mesa.mostra_mesa(mesa)

    #status: feita, testar
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op = int(self.tela_mesa.tela_opcoes())
                if op == 1:
                    self.criar_mesa()
                elif op == 2:
                    self.listar_mesa()
                elif op == 3:
                    self.abre_opcoes_alteracoes()
                elif op == 4:
                    self.excluir_mesa()
                elif op == 0:
                    continua = False
                else: 
                    self.tela_mesa.mostra_msg("opção inválida")
            except:
                self.tela_mesa.mostra_msg("opção não é um inteiro")

    #status: feito, testar 
    def abre_opcoes_alteracoes(self):
        #input seleção de mesa
        mesa = self.acha_mesa_by_num()
        if mesa == None:
            return
        else:
            continua = True
            while continua:
                try:
                    op = int(self.tela_mesa.tela_opcoes_alteraçoes(mesa))
                    if op == 1:
                        self.alterar_garçon(mesa)
                    elif op == 2:
                        mesa.controlador_conta.abre_tela_inicial()
                    elif op == 3:
                        self.encerrar_turno_garçon(mesa)
                    elif op == 0:
                        continua = False
                    else: 
                        self.tela_mesa.mostra_msg("opção inválida")
                except:
                    self.tela_mesa.mostra_msg("opção não é um inteiro")

    #status: feito, testar   
    def acha_mesa_by_num(self):
        self.listar_mesa()
        try:
            num = int(self.tela_mesa.seleciona_mesa())
            for mesa in self.mesas:
                if mesa.numero_da_mesa == num:
                    return mesa
        except:
            self.tela_mesa.mostra_msg('Não existe uma mesa com este numero')
            return

    def acha_garçon_by_cpf(self):
        self.controlador_sistema.controlador_garçon.lista_garçon()
        return self.controlador_sistema.controlador_garçon.acha_garçon_by_cpf()

    #status: feito, testar
    def alterar_garçon(self, mesa):
        if mesa.garçon != None:
            mesa.garçon.lista_de_comissao += self.contas_pagas(mesa)
        garçon_escolhido = self.acha_garçon_by_cpf()
        mesa.garçon = garçon_escolhido
        mesa.registro = mesa.registro + self.contas_pagas(mesa)
        mesa.controlador_conta.contas_pagas = []
    
    def encerrar_turno_garçon(self, mesa):
        if mesa.garçon != None:
            mesa.garçon.lista_de_comissao += self.contas_pagas(mesa)
            mesa.garçon = None
    
    #status: feita, testar 
    def listar_conta(self):
        mesa = self.acha_mesa_by_num()

        for conta in mesa.contas:
            self.tela_mesa.mostra_conta(conta)

