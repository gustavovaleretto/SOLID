from OCP.boleto import Boleto
from OCP.cartao_credito import CartaoCredito


class FormaPagamentoFactory:
    @staticmethod
    def criar_forma_pagamento( nome_forma_pagamento):
        if nome_forma_pagamento == "boleto":
            return Boleto()
        elif nome_forma_pagamento == "cartao_credito":
            return CartaoCredito()

        raise ValueError(f"Forma de pagamento {nome_forma_pagamento} não reconhecida")