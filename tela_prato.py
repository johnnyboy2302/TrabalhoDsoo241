#tela tudo ok

class TelaPrato():
    def __init__(self) -> None:
        self.__tribute = "aaaah"

    def tela_opcoes(self):
        print('-----Pratos-----')
        print('Opcoes:')
        print('1) Incluir prato')
        print('2) Alterar prato')
        print('3) Listar prato')
        print('4) Excluir prato')
        print('0) Retornar')
       
        opcao = int(input('Escolha uma opcao:'))
        return opcao
   
    def pega_dados_prato(self):
        print('-----Dados para Pratos-----')
        nome = input('Nome: ')
        preco = input('Preço: ')
        despesa = input('Despesa: ')
        codigo = input('Codigo: ')


        return {'nome':nome, 'preco':preco,
                'despesa':despesa, 'codigo':codigo}
   
    def selelciona_prato(self):
        codigo = input('Digite o codigo do prato que quer selecionar: ')
        return codigo
   
    def mostra_prato(self, dados):
        print('Nome do prato: ', {dados['nome']})
        print('Preço do prato: ', {dados['preco']})
        print('Despesa do prato: ', {dados['despesa']})
        print('Código do prato: ', {dados['codigo']})
        print('\n')

    def mostra_msg(self, mensagem):
        print(mensagem)