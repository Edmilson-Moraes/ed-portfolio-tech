# Sistema de Login com limite tentativas (3)

senha_correta = '1234'
tentativas = 0

while tentativas < 3:
    senha = input("Digite a senha:")

    if senha == senha_correta:
        print("\nSenha correta.")
        print("\nBem vindo!")
        break
    else:
        print("\nSenha incorreta, tenta novamente!\n")
    tentativas += 1

    if tentativas == 3:
        print("\nfim das tentativas. Sistema bloqueado!")
