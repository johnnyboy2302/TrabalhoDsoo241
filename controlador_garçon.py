from garçon import Garçon
from tela_garçon import TelaGarçon


class ControladorGarçon():

    def __init__(self):
        self.__tela_garçon = TelaGarçon()
        self.__garçons = []

    @property
    def garçons(self):
        return self.__garçons
    
    @property
    def tela_garçon(self):
        return self.__tela_garçon

    #status: feito, testar
    def inclui_garçon(self) -> bool:
        garçon_dados = self.tela_garçon.pega_dados_garçon()

        certo = self.testador_variaveis(garçon_dados)

        if not certo:
            self.tela_garçon.mostra_msg('Não foi possivel cadastrar este garçon:')
            self.tela_garçon.mostra_msg('parâmetros inválidos')
        else:

            duplicado = False

            novo = Garçon(certo["nome"], 
                         certo["celular"], 
                         certo["email"], 
                         certo["cpf"])

            for garçon in self.garçons:
                if garçon.cpf == novo.cpf:
                    duplicado = True
            
            if not duplicado:
                self.garçons.append(novo)
                return True
            
            else:
                self.tela_garçon.mostra_msg('Não foi possivel cadastrar este garçon:')
                self.tela_garçon.mostra_msg('Garçon já existente')
                return False

    #status: feito, testar
    def altera_garçon(self):
        #seleção do garçon a ser alterado
        garçon = self.acha_garçon_by_cpf()

        #checagem de garçon nulo
        if garçon == None:
            self.tela_garçon.mostra_msg("Não foi possível alterar este garçon, ele não existe")
            return False

        #captação de dados
        dados_alterados = self.tela_garçon.pega_dados_garçon()

        #booleano de captação bem sucedida
        certo = self.testador_variaveis(dados_alterados)

        if certo:
            garçon.nome = dados_alterados["nome"]
            garçon.celular = dados_alterados["celular"]
            garçon.email = dados_alterados["email"]
            garçon.cpf = dados_alterados["cpf"]  
            return True

        else:
            self.tela_garçon.mostra_msg("Não foi possível alterar este garçon")
            self.tela_garçon.mostra_msg("erro na captação de dados")
            return False

    #status: feito, testar
    def exclui_garçon(self):

        self.lista_garçon()
        garçon = self.acha_garçon_by_cpf()

        self.garçons.remove(garçon)
        self.tela_garçon.mostra_msg('garçon excluido')

    #status: feito, testar
    def lista_garçon(self):
        for garçon in self.garçons:
            if len(garçon.mesas) < 1:
                #isso se ele nao tiver atendendo nenhuma mesa
                self.tela_garçon.mostra_garçon({"nome": garçon.nome, "celular": garçon.celular, "email": garçon.email, "cpf": garçon.cpf}, False)
            else:
                #passei o proprio garçon pra poder chamar a funçao 'mostra_mesas' depois
                mesas_que_esta_atendendo = self.mostra_mesas(garçon)
                self.tela_garçon.mostra_garçon({"nome": garçon.nome, "celular": garçon.celular, "email": garçon.email, "cpf": garçon.cpf, "mesas": mesas_que_esta_atendendo}, True)

    #status: feito, testar
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op = int(self.tela_garçon.tela_opcoes())

            except:
                self.tela_garçon.mostra_msg("opção não é um inteiro")
                op =None

            if op == 1:
                self.inclui_garçon()

            elif op == 2:
                self.altera_garçon()

            elif op == 3:
                self.tela_garçon.espacamento()
                self.lista_garçon()

            elif op == 4:
                self.exclui_garçon()

            elif op == 5:
                self.mostrar_comissao()

            elif op == 6:
                self.atender_mesa()

            elif op == 7:
                self.remover_mesa()

            elif op == 0:
                continua = False
                
            else: 
                self.tela_garçon.mostra_msg("opção inválida")

    def mostrar_comissao(self):

        garçon = self.acha_garçon_by_cpf()

        comissao_total = 0

        for mesa in garçon.mesas:
            
            comissao_dessa_mesa = 0

            for conta in mesa.contas:

                comissao_dessa_conta = conta.comissao #temos que implementar esse atributo na conta pra facilitar
                comissao_dessa_mesa += comissao_dessa_conta

            comissao_total += comissao_dessa_mesa

        garçon.comissao = comissao_total 

        self.tela_garçon.mostra_comissao(garçon.comissao)

    #status: feito, mas so vai funcionar quando criarmos o controlador de mesa
    def atender_mesa(self):

        garçon = self.acha_garçon_by_cpf()

        mesa_para_atender = self.acha_mesa_by_num()

        duplicado = False

        for mesa in garçon.mesas:
            if mesa.numero_da_mesa == mesa_para_atender.numero_da_mesa:
                duplicado = True

        if not duplicado:
            garçon.mesas.append(mesa_para_atender)

    def remover_mesa(self):

        garçon = self.acha_garçon_by_cpf()

        self.listar_mesas(garçon)

        mesa = self.acha_mesa_by_num()

        if mesa in garçon.mesas:
            garçon.mesas.remove(mesa)
        else:
            self.tela_garçon.mostra_msg('Este garçom não está atendendo está mesa')

    #essa é só pra mostrar a que um garçon está atendendo
    def mostra_mesas(self, garçon):
        dados = []

        for mesa in garçon.mesas:
            dados.append(mesa.numero_da_mesa)

        self.tela_garçon.mostra_mesas(dados)

    #status: feito mas nao da pra testar
    def acha_mesa_by_num(self):

        achou = False

        while not achou:

            n_mesa = self.tela_garçon.seleciona_mesa()

            for mesa in controlador_mesa.mesas:

                if mesa.numero_da_mesa == n_mesa:
                    achou = True
                    return mesa
                else:
                    self.tela_garçon.mostra_msg('Não existe uma mesa com este numero, tente novamente')


    #status: feito, testar
    def acha_garçon_by_cpf(self):
        #input de código
        ok = False
        while not ok:
            try:
                cpf = str(self.tela_garçon.seleciona_garçon())
                ok = True
            except:
                self.tela_garçon.mostra_msg("O cpf deve ser uma string registrada\n")
        
        for garçon in self.garçons:
            if garçon.cpf == cpf:
                return garçon

    #status: feito, testar
    #se der certo retorna um dicionário, se der errado uma string
    def testador_variaveis(self, garçon_dados) -> dict:
        try:
            garçon_dados_checados = {"nome":str(garçon_dados["nome"]),
                                    "celular": str(garçon_dados["celular"]),
                                    "email":str(garçon_dados["email"]),
                                    "cpf":str(garçon_dados["cpf"])}
            return True
        
        except:
            return False
        
    #status: feito, só da pra testar quando a mesa e a conta tiverem prontas
