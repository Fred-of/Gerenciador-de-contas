from datetime import datetime
from controladores import criar_conta,listar_conta,excluir_conta


opcoes_menu = [
    "1- Listar contas",
    "2- Criar conta",
    "3- Atualizar conta",
    "4- Excluir conta",
    "5- Encerrar programa",
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
                controladores.listar_conta.executar()
                #...
            case '2':
                print("\n **CRIAR UMA NOVA CONTA ** \n")
                controladores.criar_conta.executar()
                #...
            case '3':
                print("\n ** ATUALIZAR UMA CONTA ** \n")
                #...
            case '4':
                print("\n ** EXCLUIR UMA CONTA ** \n")
                excluir_conta.executar()
                #...
            case '5':
                print("\n ** PROGRAMA ENCERRADO ** \n")
                #...
                break
            case _:
                print("\n OPÇÃO INVÁLIDA")


if __name__ == "__main__":
    print("\n" + datetime.now().strftime("%d/%m/%Y, %H:%M"))
    iniciar_menu()