valores = input("Entre com dois números positivos:").split()
x=int(valores[0])
y=int(valores[1])
op=input("Informe o operador:")
if op=="+":
    resultado=x+y
elif op=="-":
    resultado=x-y
elif op=="*":
    resultado=x*y
elif op=="/":
    resultado=x/y
elif op=="**":
    resultado=x**y
else:
    resultado=None
    if resultado==None:
        print(op,":Operador inexistente!!")
else:
    print(x, op, y, "=", resultado)