# Função do Usuário
def exibirCardapio():
    print("*" * 50)
    print("*** Cardápio")
    print("*" * 50)
    print("(1) Hamburger Max - R$15.00")
    print("(2) Hamburger Simples - R$8.00")
    print("(3) Batata Simples - R$13.00")
    print("(4) Finalizar Pedido")
    print("*" * 50)

def obterPreco(a) -> float:
    precos = {1:15.00, 2:8.00, 3:13.00}
    if a<1 or a>3:
        pr = 0
    else:
        pr = precos[a]
    return(pr)

# Exibir Principal
exibirCardapio()
total = 0
while True:
    op = int(input("Digite sua opção: (1), (2), (3)"))
    
