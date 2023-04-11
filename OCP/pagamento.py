class Pagamento:
    def __init__(self, valor, forma_pagamento):
        self.valor = valor
        self.forma_pagamento = forma_pagamento

    def calcular_valor_pagamento(self):
        return self.forma_pagamento.calcular_valor_pagamento(self.valor)