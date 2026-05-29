# Variáveis

estoque = [
    [1, "Molas", 30, "Prateleira 2"],
    [2, "Freio", 58, "Prateleira 1"],
    [3, "Volante", 23, "Prateleira 3"],
]


print("------ Sistema de Controle de Estoque Simplificado ------")

def adicionarProduto():
    global estoque
   
    id = input("Digite o ID do novo produto: ")
    nome = input("Digite o nome do novo produto: ")
    quantidade = input("Digite a quantidade do novo produto: ")
    localizacao = input("Digite a localização do novo produto: ")

    estoque.append([id, nome, quantidade, localizacao])
    print("Produto registrado no Sistema com sucesso!")
    print(estoque)

## Criando o menu
print("------------ Menu Interativo ------------")

while True:

    print("\n1- Adicionar produto")
    print("2- Listar todos os produtos")
    print("3- Buscar produto por ID")
    print("4- Atualizar estoque")
    print("5- Sair do programa")
    escolha = input("\nDigite a sua escolha: ")

    if escolha == "1":
        adicionarProduto()
        



