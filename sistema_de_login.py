# Sistema de Login com limite tentativas (3)
senha_correta = '1234'          # ← variável simples (string)
tentativas = 0                  # ← variável inteira que conta erros

while tentativas < 3:           # ← loop enquanto tentativas for menor que 3
    senha = input("Digite a senha:")   # ← pede a senha do usuário
    if senha == senha_correta:         # ← compara se acertou
        print("\nSenha correta.")
        print("\nBem vindo!")
        break                          # ← sai do loop imediatamente
    else:
        print("\nSenha incorreta, tenta novamente!\n")
    tentativas += 1                    # ← aumenta o contador de erro
    if tentativas == 3:                # ← só depois de 3 erros mostra mensagem final
        print("\nfim das tentativas. Sistema bloqueado!")
