#ler linhas de entrada padrão até que uma linha vizinha seja digitada.

numero=int
while numero!=" ":
    numero = int(input("Insira um número inteiro positivo"))
    print()

    if ((numero % 2) == 0) and (numero >= 0):
        for i in range(1, numero+1):
            l=[]
            if (numero%i==0):
                l.append(i)
                print("Divisores de %d são:" %numero, l)
    elif ((numero%2)!=0) and (numero>=0):
        pi=3.1415
        perimetro=2*pi*numero
        area=pi*numero**2
        print("Área e Perímetro do Círculo de Raio %d são: %0.2f e %0.2f" %(numero,area,perimetro))
    else:
        print("Programa encerrado")
#ponto de interrupção
