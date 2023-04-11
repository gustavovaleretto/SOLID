from abc import ABC, abstractmethod


class FormaPagamento(ABC):
    @abstractmethod
    def calcular_valor_pagamento(self, valor):
        pass