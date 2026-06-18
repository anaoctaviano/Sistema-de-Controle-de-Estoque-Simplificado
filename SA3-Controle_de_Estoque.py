# Variáveis

estoque = [
    [1, "Molas", 30, "Prateleira 2"],
    [2, "Freio", 58, "Prateleira 1"],
    [3, "Volante", 23, "Prateleira 3"],
]


print("------ Sistema de Controle de Estoque Simplificado ------\n")

## Criando as funções

def adicionarProduto():  ## Essa função serve para adicionar produtos na lista
    global estoque
   
    id = input("Digite o ID do novo produto: ")
    nome = input("Digite o nome do novo produto: ")
    quantidade = input("Digite a quantidade do novo produto: ")
    localizacao = input("Digite a localização do novo produto: ")

    estoque.append([id, nome, quantidade, localizacao])
    print("Produto registrado no Sistema com sucesso!")

def listarProdutos():  ## Essa função serve para listar todos os produtos
    global estoque 
    
    for produto in estoque:
        print(produto)

def buscarProdutoPorID():  ## Essa função busca um produto pelo seu ID
    global estoque

    IDprocurado = int(input("Digite o ID do produto procurado: "))
    linhaProcurada = -1

    for i in range(len(estoque)): 
        if(estoque[i][0] == IDprocurado): 
            linhaProcurada = i 
    print(f"\nO produto procurado está na linha {linhaProcurada}")
    print(f"O produto procurado é: {estoque[linhaProcurada]}")
    

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
    
    elif escolha == "2":
        listarProdutos()

    elif escolha == "3":
        buscarProdutoPorID()
        
        

## Encontrar a posição que eu quero excluir
## Excluir

## nomeProcurado = "Piran"
# linhaProcurada = -1

# for i in range(len(alunos)): ## Varre linha a linha da matriz
  #  if(alunos[i][0] == nomeProcurado): ## Verifica se a posição do nome é igual ao nome procurado
  #      linhaProcurada = i 
# print(f"\nO nome procurado está na linha {linhaProcurada}")

# print("\nExcluindo o aluno procurado: ")
# alunos.pop(linhaProcurada)
# mostrarAlunos()

