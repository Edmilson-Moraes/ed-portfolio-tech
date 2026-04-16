"""
lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar, e listar valores da sua lista. *
"""
import time
import os


# lista de compras
lista_de_compras = ['arroz', 'feijao', 'batata']

while True:

    # Verificação de estado do programa desejado pelo usuário
    verificacao_estado = input("Selecione a opção desejada para a sua Lista de Compras:\n" \
    "\t[A]dicionar [R]emover [V]erificar [S]air : ").lower()

    #verificacao de estado de lacos internos (verificacao_estado)
    opcao_laco = 'c'

    # Laco interno adicionar item
    if verificacao_estado == 'a':
        while 'c' in opcao_laco:
            lista_user = input("O que você gostaria de adicionar na sua lista de Compras?  ")
            lista_de_compras.append(lista_user)
            opcao_laco = input("\n[C]ontinuar adicionando / [S]air?").lower()
            os.system('clear')

    # laco interno remover item da lista
    elif verificacao_estado == 'r':
        while 'c' in opcao_laco:
            for i,item in enumerate(lista_de_compras):
                print("\t",i, item)
            try:
                apagar = int(input("Selecione qual item deseja apagar : \n"))
                del(lista_de_compras[apagar])
                print(f'item {lista_de_compras[apagar]} removido.')
            except ValueError:
                print("Comando inválido! Digite o número correspondente ao item que deseja apagar")
                time.sleep(2)
                os.system('clear')
                continue
            except IndexError:
                print("\n"*2, "item inexistente, selecione um item existente!","\n"*2)
                time.sleep(2)
                os.system('clear')
                continue
            opcao_laco = input("\n[C]ontinuar removendo / [S]air?").lower()
            os.system('clear')
    
    # laco interno verificar estado da lista
    elif verificacao_estado == 'v':
        print("itens da lista:\n")
        for i, item in enumerate(lista_de_compras):
            print("\t",i, item)
        print('\n')
    else:
        print("Comando inválido! digite uma opção válida!")

        
