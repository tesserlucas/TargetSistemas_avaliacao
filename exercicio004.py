# Dicionário com o faturamento por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Função para calcular o total de faturamento
def calcular_total(faturamento):
    total = sum(faturamento.values())
    return total

# Função para calcular o percentual de cada estado
def calcular_percentuais(faturamento, total):
    percentuais = {}
    for estado, valor in faturamento.items():
        percentual = (valor / total) * 100
        percentuais[estado] = percentual
    return percentuais

# Calcular o total de faturamento
total_faturamento = calcular_total(faturamento)

# Calcular os percentuais de representação
percentuais = calcular_percentuais(faturamento, total_faturamento)

# Imprimir os resultados
print("Percentual de representação de faturamento por estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

