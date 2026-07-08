from services.produtos_service import ProdutoService

def main ():
    gerente_produtos = ProdutoService()
    while True:
        print("\n--- Sistema de PDV")
        print("Escolha a opão que deseja:")
        print("Sistema do Gerente")
        print("Sistema do cliente")
        print("Encerrar sistema")

        opcao = input('Selecione a opção desejada:')

        if opcao == '1':
            print("\nAcessando sistema do Gerente")
        
        elif opcao == '2':
            print("\nAcessando sistema do cliente")

        elif opcao == '0':
            print("\nFinalizando sistema!")

        else:
            print("\nOpção inválida")

if __name__ == "__main__":
    main()