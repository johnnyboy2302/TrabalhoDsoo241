

class TelaPrato():


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
   
    def escolhe_prato(self):
        codigo = input('Digite o codigo do prato que quer selecionar: ')
        return codigo
   
    def mostra_opcoes_alterar(self):
        print('----Menu alterar----')
        print('0) Alterar nome')
        print('1) Alterar preço')
        print('2) Alterar despesa')
        print('3) Alterar codigo')
        opcao = input('Digite a opção escolhida: ')
        codigo_prato = input('Digite a alteração: ')
		
        return opcao, alteracao
   
    def mostra_prato(self, dados):
        print(f'Nome do prato: {dados['nome']}')
        print(f'Preço do prato: {dados['preco']}')
        print(f'Despesa do prato: {dados['despesa']}')
        print(f'Código do prato: {dados['codigo']}')
        print('\n')





