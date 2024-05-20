from tela_mesa import TelaMesa
from mesa import Mesa


class ControladorMesa():

    def __init__(self, controlador_sistema):
        self.__tela_mesa = TelaMesa()
        self.controlador_sistema = controlador_sistema
        self.__mesas = []

    @property
    def controlador_sistema(self):
        return self.__controlador_sistema

    @property
    def mesas(self):
        return self.__mesas
    
    @property
    def controlador_garçon(self):
        return self.__controlador_garçon
    
    @property
    def tela_mesa(self):
        return self.__tela_mesa
    
    #status: feito, testar   
    def criar_mesa(self) -> bool:
        num_mesas = len(self.mesas)

        nova_mesa = Mesa(num_mesas + 1)

        self.mesas.append(nova_mesa)

    
    #status: fazer    
    def excluir_mesa(self):
        self.listar_mesa()
        mesa = self.acha_mesa_by_num()

        if mesa in self.mesas:
            self.mesas.remove(mesa)
            self.tela_mesa.mostra_msg('Mesa excluída')
        else:
            self.tela_mesa.mostra_msg("Atenção: Mesa inexistente")


    #status: incompleta  
    def listar_mesa(self):
    
        for mesa in self.mesas:
            self.tela_mesa.mostra_mesa(mesa.numero_da_mesa)
            if mesa.garçon == None:
                self.tela_mesa.mostra_msg("Mesa sem garçon")
            else:
                if len(mesa.garçon.mesas) < 1:
                #isso se ele nao tiver atendendo nenhuma mesa
                    self.tela_mesa.mostra_garçon({"nome": mesa.garçon.nome, "celular": mesa.garçon.contato.celular, "email": mesa.garçon.contato.email, "cpf": mesa.garçon.cpf}, False)
                else:
                    #numero das mesas que ele ta atendendo
                    n_mesas_atendendo = []

                    for mesa_atendida in mesa.garçon.mesas:
                        n_mesas_atendendo.append(mesa_atendida.numero_da_mesa)
                    
                    self.tela_mesa.mostra_garçon({"nome": mesa.garçon.nome, "celular": mesa.garçon.contato.celular, "email": mesa.garçon.contato.email, "cpf": mesa.garçon.cpf, "mesas": n_mesas_atendendo}, True)

    #status: feita, testar
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op = int(self.tela_mesa.tela_opcoes())
            except:
                self.tela_mesa.mostra_msg("opção não é um inteiro")
                op = None
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

    #status: feito, testar 
    def abre_opcoes_alteracoes(self):
        continua = True
        while continua:
            try:
                op = int(self.tela_mesa.tela_opcoes_alteraçoes())
            except:
                self.tela_mesa.mostra_msg("opção não é um inteiro")
                op = None
            if op == 1:
                self.adicionar_garçon()
            elif op == 2:
                self.listar_garçon()
            elif op == 3:
                self.remover_garçon()
            elif op == 4:
                self.adicionar_conta()
            elif op == 5:
                self.listar_conta()
            elif op == 6:
                self.remover_conta()
            elif op == 0:
                continua = False
            else: 
                self.tela_mesa.mostra_msg("opção inválida")

    #status: feito, testar   
    def acha_mesa_by_num(self):
        #input de código
        certo = False
        while not certo: 
            try:
                num = self.tela_mesa.seleciona_mesa()
                certo = True
            except:
                self.tela_mesa.mostra_msg('Numero invalido, tente novamente')

        achado = None

        for mesa in self.mesas:
            if mesa.numero_da_mesa == num:
                achado = mesa

        if achado == None:
            self.tela_mesa.mostra_msg('Não existe uma mesa com este numero')
    
        return achado
    
    #status: feito, testar
    def acha_conta_by_cod(self):
        achado = False

        while not achado:
            try:
                cod = self.tela_mesa.seleciona_conta()
                for conta in self.controlador_sistema.controlador_conta.contas:
                    if conta.codigo == cod:
                        achado = True
                        return conta
                self.tela_mesa.mostra_msg('Não existe uma conta com esse codigo')
            except:
                self.tela_mesa.mostra_msg('Não foi possivel encontrar a conta')

    #status: feito, testar
    def acha_garçon_by_cpf(self):
        #input de código
        ok = False
        while not ok:
            try:
                cpf = str(self.tela_mesa.seleciona_garçon())
                ok = True
            except:
                self.tela_mesa.mostra_msg("O cpf deve ser uma string registrada\n")
        
        for garçon in self.controlador_sistema.controlador_garçon.garçons:
            if garçon.cpf == cpf:
                return garçon


    #status: feito, testar
    def adicionar_garçon(self):
    
        mesa = None

        while mesa is None:

            mesa = self.acha_mesa_by_num()

        if mesa.garçon is not None:
            self.tela_mesa.mostra_msg('Esta mesa já tem garçon')
            return None

        garçon_escolhido = self.acha_garçon_by_cpf()

        mesa.garçon = garçon_escolhido


    #status: fazer    
    def listar_garçon(self):

        for garçon in self.controlador_sistema.controlador_garçon.garçons:

            n_mesas_atendendo = []

            if len(garçon.mesas) < 1:
                #isso se ele nao tiver atendendo nenhuma mesa
                    self.tela_mesa.mostra_garçon(garçon, False, n_mesas_atendendo)
                    self.tela_mesa.espacamento()
            else:
                    #numero das mesas que ele ta atendendo

                for mesa_atendida in garçon.mesas:
                    n_mesas_atendendo.append(mesa_atendida.numero_da_mesa)
                    
                self.tela_mesa.mostra_garçon(garçon, True, n_mesas_atendendo)
                self.tela_mesa.espacamento()

    #status: fazer    
    def remover_garçon(self):
        mesa = self.tela_mesa.seleciona_mesa()
        if mesa.garçon is None:
            self.tela_mesa.mostra_msg('Esta mesa não tem um garçon')

        mesa.garçon = None

    #status: feita, testar     
    def adicionar_conta(self):
        mesa = self.acha_mesa_by_num()

        conta_para_add = self.acha_conta_by_cod()

        duplicado = False

        for conta in mesa.contas:
            if conta.codigo == conta_para_add.cod:
                duplicado = True

        if not duplicado:
            mesa.contas.append(conta_para_add)
        else:
            self.tela_mesa.mostra_msg('Esta conta já está associada a esta mesa')
    
    #status: feita, testar 
    def listar_conta(self):
        mesa = self.acha_mesa_by_num()

        for conta in mesa.contas:
            self.tela_mesa.mostra_conta(conta)

    #status: feita, testar     
    def remover_conta(self):

        mesa = self.acha_mesa_by_num()

        conta = self.acha_conta_by_cod()

        if conta in mesa.contas:
            mesa.contas.remove(conta)
        else:
            self.tela_mesa.mostra_msg('Esta conta não está associada a esta mesa')
