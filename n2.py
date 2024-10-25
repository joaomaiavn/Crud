estoque = []

while True:
    print("\nMenu:")
    print("1. Adicionar ou Atualizar Produto")
    print("2. Pesquisar Produto")
    print("3. Alterar Estoque")
    print("4. Remover Produto")
    print("5. Exibir Estoque")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")
    #Funcionalidade "Adicionar ou Atualizar Produto"
    if escolha == '1':
        nome = input("Digite o nome do produto: ")
        quantidade = int(input("Digite a quantidade: "))
        preco = float(input("Digite o preço: "))

        for produto in estoque:
            if produto[0] == nome:
                produto[1] == quantidade
                produto[2] == preco
                break 
        else:
            estoque.append([nome, quantidade, preco])
    elif escolha == "2":
            nome = input("Digite o nome do produto para pesquisar:")
            for produto in estoque:
                if produto[0] == nome:
                    print(f"produto: {produto[0]}, Quantidade: {produto[1]}, Preço: {produto[2]}")
                    break
            else:
                print("Produto não encontrado.")
    if escolha == "6":
      print("Saindo do programa.")
      break
    else:
      print("Opção inválida. Por favor, escolha uma opção válida.")
        
