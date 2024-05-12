#tela tudo ok

class TelaContato():
    def __init__(self) -> None:
        pass

    def tela_opcoes(self) -> any:
        print('-----Contatos-----')
        print('Opcoes:')
        print('1) Incluir contato')
        print('2) Alterar contato')
        print('3) Listar contatos')
        print('4) Excluir contato')
        print('0) Retornar')

        opcao = input('Escolha uma opcao:')
        return opcao
   
    def pega_dados_contato(self):
        print('-----Dados para contatos-----')
        print('OBS: o numero deve seguir o padrao "99 99999-9999"')
        celular = input('Numero: ')
        email = input('Email: ')

        return {'celular':celular, 'email':email}
   
    def seleciona_contato(self):
        celular = input('Digite o numero do contato que quer selecionar: ')
        return celular

    def mostra_contato(self, dados):
        print('Numero do contato: ', {dados['celular']})
        print('Email do contato: ', {dados['email']})
        print('\n')

    def mostra_msg(self, mensagem):
        print(mensagem)

    def espacamento(self):
        print()