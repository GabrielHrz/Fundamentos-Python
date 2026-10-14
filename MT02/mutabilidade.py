# Mutabilidade e efeitos inesperados
mensagem = {"value": 10}

saida = mensagem
saida['value'] = 0

saida = dict(mensagem)
print(f"{saida}")
