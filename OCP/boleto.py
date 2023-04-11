from abc import ABC

from OCP.forma_pagamento import FormaPagamento


class Boleto(FormaPagamento):
    def calcular_valor_pagamento(self, valor):
        return valor * 1.05