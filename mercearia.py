
produtos = []

def exibir_menu():
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Atualizar produto")
    print("4. Remover produto")
    print("5. Sair")

def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade do produto: "))
    produtos.append({"nome": nome, "preco": preco, "quantidade": quantidade})

def listar_produtos():
    for produto in produtos:
        print()
        print(f"Nome: {produto['nome']}, Preço: R$ {produto['preco']}, Quantidade: {produto['quantidade']}")
        print()

def atualizar_produto():
    nome = input("Digite o nome do produto a ser atualizado: ")
    for produto in produtos:
        if produto['nome'] == nome:
            produto['preco'] = float(input("Digite o novo preço do produto: "))
            produto['quantidade'] = int(input("Digite a nova quantidade do produto: "))


def remover_produto():
    nome = input("Digite o nome do produto a ser removido: ")
    for produto in produtos:
        if produto['nome'] == nome:
            produtos.remove(produto)


while True:
    exibir_menu()
    opcao = input("Digite sua escolha: ")

    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_produtos()
    elif opcao == "3":
        atualizar_produto()
    elif opcao == "4":
        remover_produto()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
