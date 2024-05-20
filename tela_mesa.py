from conta import Conta


class TelaMesa():
    def __init__(self):
        pass

    def tela_opcoes(self) -> any:
        print('-----Mesa-----')
        print('Opcoes:')
        print('1) Criar mesa')
        print('2) Listar mesas')
        print('3) Alterar mesa') 
        print('4) Excluir mesa')
        print('0) Retornar')

        opcao = input('Escolha uma opcao:')
        return opcao
    
    def tela_opcoes_alteraçoes(self):
        print('---Menu Alteraçoes---')
        print('Opcoes:')
        print('1) Adicionar garçon')
        print('2) Listar garçons')
        print('3) Remover garçon') 
        print('4) Adicionar conta')
        print('5) Listar contas')
        print('6) Remover conta') 
        print('0) Retornar')

    def mostra_mesa(self, n):
        print('Número da mesa: ', n)
        print('\n')

    def mostra_conta(self, conta: Conta):
        print('Código da conta:', {conta.codigo_conta})
        print('status de pagamento:', {conta.pago})
        print('Valor total: ', {conta.valor_total()})
        print('Despesas totais: ', {conta.despesa_total()})
        print('\n')

    def mostra_garçon(self, garçon, atendendo, n_mesas):
        if not atendendo:
            print('Nome do garçon: ', garçon.nome)
            print('Celular do garçon: ', garçon.contato.celular)
            print('Email do garçon: ', garçon.contato.email)
            print('Cpf do garçon: ', garçon.cpf)
            print('\n')
        else:
            print('Nome do garçon: ', garçon.nome)
            print('Celular do garçon: ', garçon.contato.celular)
            print('Email do garçon: ', garçon.contato.email)
            print('Cpf do garçon: ', garçon.cpf)
            print('Este garçon está atendendo estas mesas: ', *n_mesas)
            print('\n')

    def mostra_msg(self, msg):
        print(msg)

    def espacamento(self):
        print('\n')

    def seleciona_mesa(self):
        n_mesa = int(input('Digite o numero da mesa que quer selecionar: '))
        return n_mesa
    
    def cria_mesa(self):
        n_mesa = int(input('Digite o numero da mesa que quer selecionar: '))
        return n_mesa
    
    def seleciona_garçon(self):
        cpf = input('Digite o cpf do garçon que quer selecionar: ')
        return cpf
    
    def seleciona_conta(self):
        cod = int(input('Digite o codigo da conta que quer selecionar: '))

        return cod