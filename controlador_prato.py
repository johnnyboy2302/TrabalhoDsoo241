from prato import Prato
from tela_prato import TelaPrato
from prato_dao import PratoDAO

class ControladorPrato():
    def __init__(self):
        self.__prato_DAO = PratoDAO()
        self.__tela_prato = TelaPrato()

    @property
    def tela_prato(self):
        return self.__tela_prato

    #status: funcionando
    def inclui_prato(self) -> bool:
        prato_dados, botao = self.tela_prato.pega_dados_prato()

        certo = self.testador_variaveis(prato_dados)

        #caso a pessoa clique em cancelar
        if botao == 'Cancelar':
            return None

        if not certo:
            self.tela_prato.mostra_msg('Não foi possivel cadastrar este prato:')
            self.tela_prato.mostra_msg('parâmetros inválidos')
        else:
            duplicado = False

            novo = Prato(certo["nome"], 
                         certo["preco"], 
                         certo["despesa"], 
                         certo["codigo"])
            
            print("objeto criado")

            for prato in self.__prato_DAO.get_all():
                print("procurando na lista")
                if prato.codigo == novo.codigo:
                    print("prato unico")
                    duplicado = True
            
            if not duplicado:
                self.__prato_DAO.add(novo)
                print("prato adicionado")
                return True
            
            else:
                self.tela_prato.mostra_msg('Não foi possivel cadastrar este prato:')
                self.tela_prato.mostra_msg('código já existente')
                return False

    #status: funcionando
    def altera_prato(self):
        #seleção do prato a ser alterado
        prato = self.acha_prato_by_cod()

        if isinstance(prato, str):
            return None

        #checagem de prato nulo
        if prato == None:
            self.tela_prato.mostra_msg("Não foi possível alterar este prato, ele não existe")
            return False

        #captação de dados
        dados_alterados = self.tela_prato.pega_dados_prato()

        #booleano de captação bem sucedida
        certo = self.testador_variaveis(dados_alterados)

        if certo:
            prato.nome = certo["nome"]
            prato.preco = certo["preco"]
            prato.despesa = certo["despesa"]
            prato.codigo = certo["codigo"]  

        if isinstance(certo, str):
            self.tela_prato.mostra_msg("Não foi possível alterar este prato")
            self.tela_prato.mostra_msg("erro na captação de dados")
            return False

    #status: funcionando
    def exclui_prato(self):
        self.lista_prato()
        prato = self.acha_prato_by_cod()

        if isinstance(prato, str):
            return None

        if prato in self.__prato_DAO.get_all:
            self.__prato_DAO.remove(prato)
            self.tela_prato.mostra_msg('Prato excluido')
        else:
            self.tela_prato.mostra_msg("Atenção: Prato inexistente")

    #status: funcionando
    def lista_prato(self):

        for prato in self.__prato_DAO.get_all():
            self.tela_prato.mostra_prato({"nome": prato.nome, "preco": prato.preco, "despesa": prato.despesa, "codigo": prato.codigo})

    #status: funcionando
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                #to trazendo o botao junto
                op, botao = self.tela_prato.tela_opcoes()
                int(op)

            except:
                self.tela_prato.mostra_msg("Nenhuma opção foi escolhida")
                op = None

            if op == 1:
                self.inclui_prato()

            elif op == 2:
                self.altera_prato()

            elif op == 3:
                #self.tela_prato.espacamento()
                self.lista_prato()

            elif op == 4:
                self.exclui_prato()
            #caso o botao seja o cancelar
            elif op == 0 or botao == 'Cancelar':
                continua = False
                
            else: 
                self.tela_prato.mostra_msg("opção inválida")

    #status: funcionando
    def acha_prato_by_cod(self) -> Prato:
        #input de código

        cod, botao = self.tela_prato.seleciona_prato()

        #caso a pessoa cancele, vou retornar o botao
        #teremos que testar se é str em todas funçoes que usam essa funçao
        if botao == 'Cancelar':
            return botao

        ok = False
        while not ok:
            try:
                int(cod)
                ok = True
            except:
                self.tela_prato.mostra_msg("O código deve ser um inteiro registrado\n")
        

        for prato in self.__prato_DAO.get_all():
            print(prato.codigo)
            if prato.codigo == cod:
                return prato

    
    def testador_variaveis(self, prato_dados) -> dict:
        try:
            prato_dados_checados = {"nome":str(prato_dados["nome"]),
                                    "preco": float(prato_dados["preco"]),
                                    "despesa":float(prato_dados["despesa"]),
                                    "codigo":int(prato_dados["codigo"])}
            return True
        
        except:
            return False