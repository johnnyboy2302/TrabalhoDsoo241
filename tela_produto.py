class TelaProduto():
    def __init__(self):
        pass

    def tela_opcoes(self) -> any:
        print('-----Produtos-----')
        print('Opcoes:')
        print('1) cadastro de bebidas')
        print('2) cadastro de pratos')
        print('0) Retornar')
        opcao = input('Escolha uma opcao:')
        return opcao
    
    def mostra_msg(self, mensagem):
        print(mensagem)