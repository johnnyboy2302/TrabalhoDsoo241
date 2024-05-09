class TelaConta():
    def __init__(self):
        pass

    def tela_opcoes(self) -> any:
        print('-----Conta-----')
        print('Opcoes:')
        print('1) Criar conta')
        print('2) Adicionar um produto')
        print('4) Remover Produto')
        print('5) Pagar a conta')
        print('6) Mostrar contas')
        print('7) Deletar conta')
        print('0) Retornar')

        opcao = input('Escolha uma opcao:')
        return opcao
    
    