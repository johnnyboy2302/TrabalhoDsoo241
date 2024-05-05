from prato import Prato
from tela_prato import TelaPrato

class ControladorPrato():
    def __init__(self):
        self.__tela_prato = TelaPrato()
        self.__pratos = []

    @property
    def pratos(self):
        return self.__pratos
    
    @property
    def tela_prato(self):
        return self.__tela_prato

    def inclui_prato(self) -> bool:
        duplicado = False

        prato_dados = self.tela_prato.pega_dados_prato()

        certo = self.testador_variaveis(prato_dados)

        if not certo:
            self.tela_prato.mostra_msg('Não foi possivel cadastrar este prato')
        else:

            novo = Prato(prato_dados["nome"], prato_dados["preco"], prato_dados["despesa"], prato_dados["codigo"])

            for prato in self.pratos:
                if novo.codigo == prato.codigo:
                    duplicado = True

        if not duplicado:
            self.pratos.append(novo)
            return True
        else:
            self.tela_prato.mostra_msg('Não foi possivel cadastrar este prato, há um erro')
            return False
        
    def altera_prato(self):

        prato = self.pega_cod_e_acha_prato()

        dados_alterados = self.tela_prato.pega_dados_prato()

        certo = self.testador_variaveis(dados_alterados)

        if not certo:
            self.tela_prato.mostra_msg("Não foi possível alterar este prato, há erros no input dos dados")
            #é assim que saio do metodo?
            exit()

        if (prato is not None):
            prato.nome = dados_alterados["nome"]
            prato.preco = dados_alterados["preco"]
            prato.despesa = dados_alterados["despesa"]
            prato.codigo = dados_alterados["codigo"]
        else:
            self.tela_prato.mostra_msg("Não foi possível alterar este prato, ele não existe")


    def exclui_prato(self):
        self.lista_prato()
        prato = self.pega_cod_e_acha_prato()

        if(prato is not None):
            self.pratos.remove(prato)
            self.tela_prato.mostra_msg('Prato excluido')
        else:
            self.tela_prato.mostra_msg("ATENCAO: Prato não existente")

    def lista_prato(self):

        for prato in self.pratos:
            self.tela_prato.mostra_prato({"nome": prato.nome, "preco": prato.preco, "despesa": prato.despesa, "codigo": prato.codigo})

    def abre_tela_inicial(self):

        continua = True
        while continua:
            op = self.tela_prato.tela_opcoes()
            if op == 1:
                self.inclui_prato()
            elif op == 2:
                self.altera_prato()
            elif op == 3:
                self.lista_prato()
            elif op == 4:
                self.exclui_prato()
            elif op == 0:
                continua = False
            else: 
                self.tela_prato.mostra_msg("opção inválida")


    def pega_cod_e_acha_prato(self):
        #aqui eu to pegando o codigo do prato 
        cod = self.tela_prato.seleciona_prato()

        for prato in self.pratos:
            if prato.codigo == cod:
                return prato
            
    def retorna(self):
        self.__controlador_sistema.abre_tela()

    #criei aquela funcao de verificacao que a gente conversou
    def testador_variaveis(self, prato_dados):
        
        nome = prato_dados["nome"]
        nome_ok = isinstance(nome, str)
        preco = prato_dados["preco"]
        preco_ok = isinstance(preco, float or int)
        despesa = prato_dados["despesa"]
        despesa_ok = isinstance(despesa, float or int)
        codigo = prato_dados["codigo"]
        codigo_ok = isinstance(codigo, int)
        if nome_ok and preco_ok and despesa_ok and codigo_ok:
            return True
        else:
            return False