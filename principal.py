from datetime import datetime
from controladores import (criar_conta, excluir_conta, listar_conta,atualizar_conta, gerar_retorio)
from os import (system, name) 

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

opcoes_menu = [
    "1- Listar contas",
    "2- Criar conta",
    "3- Atualizar conta",
    "4- Excluir conta",
    "5 - Gerar relatório do mês",
    "6- Encerrar programa",
]

def iniciar_menu():
    while True:
        print("\n- MENU PRINCIPAL -\n")

        for opcao in opcoes_menu:
            print(opcao)

        opcao_escolhida = input("\n Digite uma opção: ")

        match opcao_escolhida:
            case '1':
                print("\n ** LISTAR CONTAS ** \n")
                listar_conta.executar()
                #...
            case '2':
                print("\n **CRIAR UMA NOVA CONTA ** \n")
                criar_conta.executar()
                #...
            case '3':
                print("\n ** ATUALIZAR UMA CONTA ** \n")
                atualizar_conta.executar()
                #...
            case '4':
                print("\n ** EXCLUIR UMA CONTA ** \n")
                excluir_conta.executar()
                #...
            case '5':
                print("\n ** GERAÇÃO DE RELATÓRIO ** \n")
                gerar_retorio.executar()
                #...
                
            case '6':
                print("\n ** PROGRAMA ENCERRADO ** \n")
                #...
                break
            case _:
                print("\n OPÇÃO INVÁLIDA")


if __name__ == "__main__":
    limpa_tela()
    print("\n" + datetime.now().strftime("%d/%m/%Y, %H:%M"))
    iniciar_menu()