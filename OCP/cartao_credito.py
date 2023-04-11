from OCP.forma_pagamento import FormaPagamento


class CartaoCredito(FormaPagamento):
    def calcular_valor_pagamento(self, valor):
        return valor * 1.1