from OCP.forma_pagamento_factory import FormaPagamentoFactory
from OCP.pagamento import Pagamento

pagamento_boleto = Pagamento(100, FormaPagamentoFactory.criar_forma_pagamento("boleto"))
valor_pagamento_boleto = pagamento_boleto.calcular_valor_pagamento()
print(f"Valor do pagamento no boleto: {valor_pagamento_boleto}")

pagamento_cartao = Pagamento(100, FormaPagamentoFactory.criar_forma_pagamento("cartao_credito"))
valor_pagamento_cartao = pagamento_cartao.calcular_valor_pagamento()
print(f"Valor do pagamento no cartão de crédito: {valor_pagamento_cartao}")
