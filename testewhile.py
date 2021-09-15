indice = 1 # inicializa variável
while indice <= 10: # testa condição
    print(indice, end=' ')
    indice = indice + 1
print()

#fatorial
num = int(input('Digite um valor inteiro e positivo:'))
i = 1
fat = 1
while i <= num:
    fat = fat * i
    i = i + 1
print('O fatorial de', num, '=', fat)