import json

# Função para ler os dados do JSON
def ler_dados():
    with open('faturamento.json', 'r') as arquivo:
        dados = json.load(arquivo)
        return dados['faturamento']

# Função principal para calcular os valores solicitados
def calcular_estatisticas():
    faturamentos = ler_dados()
    valores = [f['valor'] for f in faturamentos if f['valor'] > 0]
    
    if not valores:
        print("Não houve faturamento em dias válidos.")
        return

    menor_valor = min(valores)
    maior_valor = max(valores)
    media = sum(valores) / len(valores)
    dias_acima_da_media = sum(1 for v in valores if v > media)

    print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

# Executando a função principal
if __name__ == "__main__":
    calcular_estatisticas()
