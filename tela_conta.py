class TelaConta():
    def __init__(self):
        pass

    def tela_opcoes(self) -> any:
        print('-----Conta-----')
        print('Opcoes:')
        print('1) Criar conta')
        print('2) Adicionar um produto') #listar os produtos disponiveis antes de adicionar
        print('3) Remover um produto')
        print('4) Listar produtos de uma conta')
        print('5) Pagar a conta') 
        print('6) Mostrar contas') 
        print('7) Mostrar contas pagas') 
        print('8) Deletar conta')
        print('0) Retornar')

        opcao = input('Escolha uma opcao:')
        return opcao
    
    def mostra_produto(self, dados_produto, produto):

        if isinstance(produto, Prato):
            print('Nome do prato: ', {dados_produto['nome']})
            print('Preço do prato: ', {dados_produto['preco']})
            print('Despesa do prato: ', {dados_produto['despesa']})
            print('Código do prato: ', {dados_produto['codigo']})
            print('\n')

        elif isinstance(produto, Bebida):
            print('Nome da bebida: ', {dados_produto['nome']})
            print('Preço da bebida: ', {dados_produto['preco']})
            print('Despesa da bebida: ', {dados_produto['despesa']})
            print('Código da bebida: ', {dados_produto['codigo']})
            print('\n')
    
    def mostra_conta(self, dados_conta):
        print('Código da conta: ', {dados_conta['codigo']})
        print('A conta foi paga? ', {dados_conta['pago']})
        print('Valor total: ', {dados_conta['valor_total']})
        print('Despesas totais: ', {dados_conta['despesa_total']})
        print('\n')

    def seleciona_conta(self):
        cod = int(input('Digite o código da conta: '))

        return cod
    
    def seleciona_produto(self):
        cod = int(input('Digite o código do produto: '))

        return cod
    
    def mostra_msg(self, msg):
        print(msg)

    
    