from services.produtos_service import ProdutoService

def ler_int(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um número inteiro válido.")

def ler_float(mensagem):
    while True:
        try:
            valor = input(mensagem).replace(",", ".")
            return float(valor)
        except ValueError:
            print("Digite um número válido. Ex: 29.90")

def ler_float_positivo(mensagem):
    while True:
        positivo = ler_float(mensagem)

        if positivo > 0:
            return positivo
        
        print("Digite um valor acima de 0.")

def ler_int_nao_negativo(mensagem):
    while True:
        int_positivo = ler_int(mensagem)

        if int_positivo >= 0:
            return int_positivo

        print("Digite um valor acima de 0.")


def ler_texto_obrigatorio(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto:
            return texto

        print("Este campo não pode ficar vazio.")

def ler_int_positivo(mensagem):
    while True:
        int_adiocionar = ler_int(mensagem)

        if int_adiocionar > 0:
            return int_adiocionar

        print("Digite um valor maior que 0.")

def confirmar_acao(mensagem):
    while True:
        reposta = input(mensagem).strip().lower()

        if resposta == "sim":
            return True

        elif resposta == "nao":
            return False

        print("Digite apenas sim ou nao")

def mostrar_produto(produto):
    print("-" * 40)
    print(f"Código: {produto.codigo}")
    print(f"Nome: {produto.nome}")
    print(f"Preço: R$ {produto.preco:.2f}")
    print(f"Estoque: {produto.estoque}")
    print(f"Categoria: {produto.categoria}")
    print(f"Tamanho: {produto.tamanho}")
    print(f"Cor: {produto.cor}")
    print(f"Imagem: {produto.imagem_url}")


def mostrar_produtos(produtos):
    if not produtos:
        print("Nenhum produto encontrado.")
        return

    for produto in produtos:
        mostrar_produto(produto)


def main():
    produtos_service = ProdutoService()

    while True:
        print("\n--- Sistema do Gerente ---")
        print("1. Cadastrar produto")
        print("2. Listar todos os produtos")
        print("3. Buscar produto por código")
        print("4. Buscar produto por categoria")
        print("5. Atualizar produto")
        print("6. Excluir produto")
        print("7. Adicionar estoque")
        print("8. Baixar estoque")
        print("9. Ver produtos com estoque baixo")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = ler_texto_obrigatorio("Nome do produto: ")
            preco = ler_float_positivo("Preço do produto: ")
            estoque = ler_int_nao_negativo("Quantidade em estoque: ")
            categoria = ler_texto_obrigatorio("Categoria do produto: ")

            tamanho = input("Tamanho, se tiver: ") or None
            cor = input("Cor, se tiver: ") or None
            imagem_url = input("URL ou caminho da imagem: ") or None

            produtos_service.cadastrar_produto(
                nome,
                preco,
                estoque,
                categoria,
                tamanho,
                cor,
                imagem_url
            )

            print("Produto cadastrado com sucesso!")

        elif opcao == "2":
            produtos = produtos_service.listar_todos()
            mostrar_produtos(produtos)

        elif opcao == "3":
            codigo = ler_int("Digite o código do produto: ")
            produto = produtos_service.buscar_por_codigo(codigo)

            if produto is None:
                print("Produto não encontrado.")
            else:
                mostrar_produto(produto)

        elif opcao == "4":
            categoria = input("Digite a categoria: ")
            produtos = produtos_service.listar_por_categoria(categoria)
            mostrar_produtos(produtos)

        elif opcao == "5":
            codigo = ler_int("Código do produto que deseja atualizar: ")
            produto = produtos_service.buscar_por_codigo(codigo)

            if produto is None:
                print("Produto não encontrado.")
            else:
                print("\nProduto atual:")
                mostrar_produto(produto)

                print("\nDigite os novos dados do produto:")

                nome = input("Novo nome: ")
                preco = ler_float("Novo preço: ")
                estoque = ler_int("Novo estoque: ")
                categoria = input("Nova categoria: ")

                tamanho = input("Novo tamanho, se tiver: ") or None
                cor = input("Nova cor, se tiver: ") or None
                imagem_url = input("Nova URL ou caminho da imagem: ") or None

                atualizado = produtos_service.atualizar_produto(
                    codigo,
                    nome,
                    preco,
                    estoque,
                    categoria,
                    tamanho,
                    cor,
                    imagem_url
                )

                if atualizado:
                    print("Produto atualizado com sucesso!")
                else:
                    print("Não foi possível atualizar o produto.")

        elif opcao == "6":
            codigo = ler_int("Código do produto que deseja excluir: ")

            confirmar = confirmar_acao(
                "Tem certeza que deseja excuir este produto? (sim / nao)"
            )

            if confirmar:
                excluido = produtos_service.excluir_produto(codigo)

                if excluido:
                    print("Produto excluido com sucesso")

                else:
                    print("Produto não encontrado")

            else:
                print("Exclusão cancelada")

        elif opcao == "7":
            codigo = ler_int("Código do produto: ")
            quantidade = ler_int_positivo("Quantidade para adicionar ao estoque: ")

            atualizado = produtos_service.adicionar_estoque(codigo, quantidade)

            if atualizado:
                print("Estoque atualizado com sucesso!")
            else:
                print("Produto não encontrado.")

        elif opcao == "8":
            codigo = ler_int("Código do produto: ")
            quantidade = ler_int_positivo("Quantidade para baixar do estoque: ")

            status = produtos_service.baixar_estoque(codigo, quantidade)

            if status == "ok":
                print("Estoque baixado com sucesso!")
            elif status == "produto_nao_encontrado":
                print("Produto não encontrado.")
            elif status == "estoque_insuficiente":
                print("Estoque insuficiente.")

        elif opcao == "9":
            limite = ler_int("Mostrar produtos com estoque menor ou igual a: ")
            produtos = produtos_service.listar_estoque_baixo(limite)
            mostrar_produtos(produtos)

        elif opcao == "0":
            print("Saindo do sistema do gerente...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()