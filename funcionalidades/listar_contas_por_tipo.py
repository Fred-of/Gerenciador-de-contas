import servicos
import servicos.obter_contas

def executar(tipo):
   
    contas = servicos.obter_contas.executar()

    conta_filtradas = []
    if tipo != "todos":
        # for conta in contas:
        #     if conta.get("tipo","") == tipo:
        #         conta_filtradas.append(conta)
        # contas = conta_filtradas
        contas = [conta for conta in contas if conta.get("tipo","") == tipo]


    for conta in contas:
        print("\n ------ // ------")
        for chave, valor in conta.items():
            print(f"{chave}: {"(vazio)" if len(valor) == 0 else valor}")

