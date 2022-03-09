n=int(input())
print(n)

nota100=n//100
n=n-nota100*100

nota50=n//50
n=n-nota50*50


nota20=n//20
n=n-nota20*20

nota10=n//10
n=n-nota10*10

nota5=n//5
n=n-nota5*5

nota2=n//2
n=n-nota2*2

nota1=n//1
n=n-nota1*1


print("{} nota(s) de R$ 100,00".format(nota100))
print("{} nota(s) de R$ 50,00".format(nota50))
print("{} nota(s) de R$ 20,00".format(nota20))
print("{} nota(s) de R$ 10,00".format(nota10))
print("{} nota(s) de R$ 5,00".format(nota5))
print("{} nota(s) de R$ 2,00".format(nota2))
print("{} nota(s) de R$ 1,00".format(nota1))

