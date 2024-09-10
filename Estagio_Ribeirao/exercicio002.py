string = input("Digite uma string: ")

string_lower = string.lower()

if 'a' in string_lower:
    count = string_lower.count('a')
    print(f"A letra 'a' aparece {count} vezes na string.")
else:
    print("A letra 'a' não foi encontrada na string.")
