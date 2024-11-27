from servicos import obter_contas, atualizar_contas

def executar(id_conta):

    contas = obter_contas.executar()
    conta_encontrada =  None

    for conta in contas:
        if conta.get("id") == id_conta:
            conta_encontrada = conta

        if conta_encontrada is None:
            print(f"Nenhuma conta foi encontrada com o ID {id_conta}")
            return
        
        print("\n -- Conta Encontrada --")
        for chave, valor in conta_encontrada.items():
            print(f"{chave}: {"(vazio)" if len(valor) == 0 else valor}")

        escolha = input("\nDeseja excluir essa conta? (s/n): ")

        if escolha.lower != "s":
            print("Operação cancelada")
            return
        
        contas_filtradas = [conta for conta in contas if conta.get("id") != id_conta]

        atualizar_contas.executar(contas_filtradas)
        if foi_deletado:
            print("Conta excluída com sucesso")
        else:
            print("Falha ao excluir a conta!")