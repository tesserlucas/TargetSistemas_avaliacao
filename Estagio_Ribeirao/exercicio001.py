n = int(input('Inserir numero para gerar a sequência de Fibonnaci :'))

n1 = 1
n2 = 1
count = 0

lista = [0,1,1]

for vic in range(0, n):
    count = n1 + n2
    n1 = count
    n2 = (count - n2)
    lista.append(count)

print(lista)

validacao = int(input('\n Verificar se existe na sequência de Fibonnaci acima: '))

if(validacao in lista):
    print('\n O número {} existe na sequência acima'.format(validacao))
else:
    print('\n O número {} não existe na sequência acima'.format(validacao))