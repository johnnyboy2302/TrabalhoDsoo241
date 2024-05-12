from contato import Contato
from tela_contato import TelaContato
from controlador_sistema import ControladorSistema

class Controladorcontato():
    def __init__(self):
        self.__tela_contato = TelaContato()
        self.__contatos = []
        self.__controlador_sistema = ControladorSistema()

    @property
    def contatos(self):
        return self.__contatos
    
    @property
    def tela_contato(self):
        return self.__tela_contato

    #status: temos que pensar, porque teoricamente o contato é criado dentro de uma pessoa
    def inclui_contato(self) -> bool:
        contato_dados = self.tela_contato.pega_dados_contato()

        certo = self.testador_variaveis(contato_dados)

        if not certo:
            self.tela_contato.mostra_msg('Não foi possivel cadastrar esta contato:')
            self.tela_contato.mostra_msg('parâmetros inválidos')

        else:
            duplicado = False

            novo = Contato(contato_dados["celular"], contato_dados['email'])

            for contato in self.contatos:
                if contato.celular == novo.celular:
                    duplicado = True
            
            if not duplicado:
                self.contatos.append(novo)
                self.tela_contato.mostra_msg('Contato incluido com sucesso')
            
            else:
                self.tela_contato.mostra_msg('Não foi possivel cadastrar este contato: ')
                self.tela_contato.mostra_msg('Celular já existente')
                return False

    #status: feito, testar
    def altera_contato(self):
        #seleção do contato a ser alterado
        contato = self.acha_contato_by_num()

        #checagem de contato nulo
        if contato == None:
            self.tela_contato.mostra_msg("Não foi possível alterar este contato, ele não existe")

        #captação de dados
        dados_alterados = self.tela_contato.pega_dados_contato()

        #booleano de captação bem sucedida
        certo = self.testador_variaveis(dados_alterados)

        if certo:
            contato.celular = dados_alterados["celular"]
            contato.email = dados_alterados["email"]
            self.tela_contato.mostra_msg('Contato alterado com sucesso')

        else:
            self.tela_contato.mostra_msg("Não foi possível alterar esta contato")
            self.tela_contato.mostra_msg("erro na captação de dados")

    #status: feito, testar
    def exclui_contato(self):
        self.lista_contato()
        contato = self.acha_contato_by_num()

        if contato in self.contatos:
            self.contatos.remove(contato)
            self.tela_contato.mostra_msg('contato excluído')
        else:
            self.tela_contato.mostra_msg("Atenção: contato inexistente")

    #status: feito, testar
    def lista_contato(self):
        for contato in self.contatos:
            self.tela_contato.mostra_contato({"celular": contato.celular, "email": contato.email})

    #status: feita, testar
    def abre_tela_inicial(self):
        continua = True
        while continua:
            try:
                op = int(self.tela_contato.tela_opcoes())
            except:
                self.tela_contato.mostra_msg("opção não é um inteiro")
                op = None
            if op == 1:
                self.inclui_contato()
            elif op == 2:
                self.altera_contato()
            elif op == 3:
                self.tela_contato.espacamento()
                self.lista_contato()
            elif op == 4:
                self.exclui_contato()
            elif op == 0:
                continua = False
            else: 
                self.tela_contato.mostra_msg("opção inválida")

    #status: feito, testar
    def acha_contato_by_num(self):
        #input de código
        num = self.tela_contato.seleciona_contato()
        
        achado = None

        for contato in self.contatos:
            if contato.celular == num:
                achado = contato

        if achado == None:
            self.tela_contato.mostra_msg('Numero nao reconhecido')
    
        return achado

    #status: feito
    def retorna(self):
        self.__controlador_sistema.abre_tela_inicial()

    #status: feito, testar
    #se der certo retorna True, se der errado False
    def testador_variaveis(self, contato_dados) -> dict:
        try:
            contato_dados_checados = {"celular":str(contato_dados["celular"]), 'email':str(contato_dados['email'])}
            return True
        
        except:
            return False