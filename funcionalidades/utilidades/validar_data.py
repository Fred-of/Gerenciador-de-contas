from datetime import datetime
from funcionalidades.utilidades import validar_data


def  executar(data):
    if len(data_pagamento) == 0:
        data_pagamento = datetime.today().strftime("%d/%m/%Y")
    return data