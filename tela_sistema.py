class TelaSistema:
    #fazer aqui tratamento dos dados, caso a entrada seja diferente do esperado
    def tela_opcoes(self):
        print("-------- Sistema do restaurante ---------")
        print("Escolha sua opcao")
        print("1 - Produtos")
        print("2 - Contas")
        print("3 - Contatos")
        print("4 - Garçons")
        print("0 - Finalizar sistema")
        opcao = int(input("Escolha a opcao:"))
        return opcao
    
    def mostra_msg(msg):
        print(msg)
