# Sistema de Login com limite tentativas (3)

MAX_TENTATIVAS = 3
SENHA_CORRETA = "1234"

def autenticar():
    tentativas = 0

    while tentativas < MAX_TENTATIVAS:
        senha = input("Digite a senha: ")

        if validar_senha(senha):
            print("\nAcesso autorizado.")
            return True
        else:
            tentativas +=1
            print(f"Senha incorreta! Tentativa {tentativas}/{MAX_TENTATIVAS}.\n")

        print("Sistema bloqueado!")
        return False
    
def validar_senha(senha):
    return senha == SENHA_CORRETA

if __name__ == "__main__":
    autenticar()
