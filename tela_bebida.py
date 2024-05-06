#tela tudo ok

class TelaBebida():
    def __init__(self) -> None:
        pass

    def tela_opcoes(self) -> any:
        print('-----Bebidas-----')
        print('Opcoes:')
        print('1) Incluir bebida')
        print('2) Alterar bebida')
        print('3) Listar bebidas')
        print('4) Excluir bebida')
        print('0) Retornar')

        opcao = input('Escolha uma opcao:')
        return opcao
   
    def pega_dados_bebida(self):
        print('-----Dados para bebidas-----')
        nome = input('Nome: ')
        preco = input('Preço: ')
        despesa = input('Despesa: ')
        codigo = input('Codigo: ')

        return {'nome':nome, 'preco':preco,
                'despesa':despesa, 'codigo':codigo}
   
    def seleciona_bebida(self):
        codigo = int(input('Digite o codigo da bebida que quer selecionar: '))
        return codigo

    def mostra_bebida(self, dados):
        print('Nome da bebida: ', {dados['nome']})
        print('Preço da bebida: ', {dados['preco']})
        print('Despesa da bebida: ', {dados['despesa']})
        print('Código da bebida: ', {dados['codigo']})
        print('\n')

    def mostra_msg(self, mensagem):
        print(mensagem)

    def espacamento(self):
        print()