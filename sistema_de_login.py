# Sistema de Login Militar - Versão 2
# Implementação de dicionário para usuários e senhas

user_pass = {

    "edmilson" : "fuzileiro123",
    "leidiane" : "amoramoramor",
    "manuela" : "catimbau",
}

tentativas = 0      # contador de tentativas
max_tentativas = 3  # n° máx de tentativas

while tentativas < 3:
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

# Verifica se o usuário existe NO dicionário E se a senha bate
    if usuario in user_pass and user_pass[usuario] == senha:
        print(f"\nAcesso liberado! Bem-vindo, {usuario.capitalize()}!") 
        break # sai do loop

    else:
        tentativas +=1
        restantes = max_tentativas - tentativas
        print(f"\nCredenciais erradas. Tentativas restantes: {restantes}")

# Fora do loop: só chega aqui se estogar as tentativas

if tentativas == max_tentativas:
    print("\n!!!ACESSO NEGADO!!!")
    print("\nMáximo de tentativas atingido.")
