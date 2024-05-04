from prato import Prato

class ControladorPrato():
    def _init_(self):
        self.__tela_prato = TelaPrato(self)
        self.__pratos = []

    @property
    def pratos(self):
        return self.__pratos
    
    @property
    def tela_prato(self):
        return self.__tela_prato

    def inclui_prato(self) -> bool:
        duplicado = False
        prato_dados = self.__tela_prato.pega_dados_prato()
        nome = prato_dados["nome"]
        nome_ok = isinstance(nome, str)
        preco = prato_dados["preco"]
        preco_ok = isinstance(preco, float and int)
        despesa = prato_dados["despesa"]
        despesa_ok = isinstance(despesa, float and int)
        codigo = prato_dados["codigo"]
        codigo_ok = isinstance(codigo, int)
        if nome_ok and preco_ok and despesa_ok and codigo_ok:
            novo = Prato(nome, preco, despesa, codigo)
        for prato in self.pratos:
            if novo.codigo == prato.codigo:
                duplicado = True
        if not duplicado:
            self.pratos.append(novo)
            return True
        return False
        
    def altera_prato(self):

        #chamei essa que chama aquela e consegue o prato para alterar
        prato = self.acha_prato_por_codigo()

        dados_alterados = self.tela_prato.pega_dados_prato()

        

    
    def exclui_prato(self):

    def lista_prato(self):

    def finalizar(self):

    def abre_tela_inicial(self):

    def acha_prato_por_codigo(self):
        #aqui eu to pegando o codigo do prato 
        cod = self.tela_prato.seleciona_prato()

        for prato in self.pratos:
            if prato.codigo == cod:
                return prato
            
        
            