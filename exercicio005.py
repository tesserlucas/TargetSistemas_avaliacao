def inverter_string(s):
    # Inicializa uma string vazia para armazenar o resultado
    string_invertida = ''
    # Percorre a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

# Solicita a entrada do usuário
entrada = input("Digite uma string para ser invertida: ")

# Chama a função para inverter a string
resultado = inverter_string(entrada)

# Exibe o resultado
print("String invertida:", resultado)
