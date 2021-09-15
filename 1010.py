produto1=input().split()
cod1=int(produto1[0])
qtd1=int(produto1[1])
valor1=float(produto1[2])

produto2=input().split()
cod2=int(produto2[0])
qtd2=int(produto2[1])
valor2=float(produto2[2])

valorTotal = qtd1*valor1 + qtd2*valor2
print("VALOR A PAGAR: R$ %0.2f" %valorTotal)