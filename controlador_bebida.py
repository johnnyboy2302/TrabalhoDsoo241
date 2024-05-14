from bebida import Bebida
from tela_bebida import TelaBebida

class ControladorBebida():
    def __init__(self):
        self.__tela_bebida = TelaBebida()
        self.__bebidas = []

    @property
    def bebidas(self):
        return self.__bebidas
    
    @property
    def tela_bebida(self):
        return self.__tela_bebida

    #status: funcionando
    def inclui_bebida(self) -> bool:
        bebida_dados = self.tela_bebida.pega_dados_bebida()

        certo = self.testador_variaveis(bebida_dados)

        if isinstance(certo, str):
            self.tela_bebida.mostra_msg('Não foi possivel cadastrar esta bebida:')
            self.tela_bebida.mostra_msg('parâmetros inválidos')

        else:
            duplicado = False

            novo = Bebida(certo["nome"], 
                         certo["preco"], 
                         certo["despesa"], 
                         certo["codigo"])

            for bebida in self.bebidas:
                if bebida.codigo == novo.codigo:
                    duplicado = True
            
            if not duplicado:
                self.bebidas.append(novo)
                return True
            
            else:
                self.tela_bebida.mostra_msg('Não foi possivel cadastrar este bebida:')
                self.tela_bebida.mostra_msg('código já existente')
                return False

    #status: funcionando
    def altera_bebida(self):
        #seleção do bebida a ser alterado
        bebida = self.acha_bebida_by_cod()

        #checagem de bebida nulo
        if bebida == None:
            self.tela_bebida.mostra_msg("Não foi possível alterar esta bebida, ela não existe")
            return False

        #captação de dados
        dados_alterados = self.tela_bebida.pega_dados_bebida()

        #booleano de captação bem sucedida
        certo = self.testador_variaveis(dados_alterados)

        if certo:
            bebida.nome = certo["nome"]
            bebida.preco = certo["preco"]
            bebida.despesa = certo["despesa"]
            bebida.codigo = certo["codigo"]  

        if isinstance(certo, str):
            self.tela_bebida.mostra_msg("Não foi possível alterar esta bebida")
            self.tela_bebida.mostra_msg("erro na captação de dados")
            return False

    #status: funcionando
    def exclui_bebida(self):
        self.lista_bebida()
        bebida = self.acha_bebida_by_cod()

        if bebida in self.bebidas:
            self.bebidas.remove(bebida)
            self.tela_bebida.mostra_msg('bebida excluída')
        else:
            self.tela_bebida.mostra_msg("Atenção: bebida inexistente")

    #status: ainda não chequei
    def lista_bebida(self):
        for bebida in self.bebidas:
            self.tela_bebida.mostra_bebida({"nome": bebida.nome, "preco": bebida.preco, "despesa": bebida.despesa, "codigo": bebida.codigo})

    #status: funcionando
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op = int(self.tela_bebida.tela_opcoes())
            except:
                self.tela_bebida.mostra_msg("opção não é um inteiro")
                op = None
            if op == 1:
                self.inclui_bebida()
            elif op == 2:
                self.altera_bebida()
            elif op == 3:
                self.tela_bebida.espacamento()
                self.lista_bebida()
            elif op == 4:
                self.exclui_bebida()
            elif op == 0:
                continua = False
            else: 
                self.tela_bebida.mostra_msg("opção inválida")

    #status: funcionando
    def acha_bebida_by_cod(self) -> Bebida:
        #input de código
        ok = False
        while not ok:
            try:
                cod = int(self.tela_bebida.seleciona_bebida())
                ok = True
            except:
                self.tela_bebida.mostra_msg("código deve ser um inteiro registrado\n")
        

        for bebida in self.bebidas:
            if bebida.codigo == cod:
                return bebida

    #status: inutilizada no momento --> rever 
    """def retorna(self):
        self.__controlador_sistema.abre_tela_inicial()"""

    #status: funcionando
    #se der certo retorna um dicionário, se der errado uma string
    def testador_variaveis(self, bebida_dados) -> dict:
        try:
            bebida_dados_checados = {"nome":str(bebida_dados["nome"]),
                                    "preco": float(bebida_dados["preco"]),
                                    "despesa":float(bebida_dados["despesa"]),
                                    "codigo":int(bebida_dados["codigo"])}
            return bebida_dados_checados
        
        except:
            return "falha na verificação"