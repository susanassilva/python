i=1
par=0
impar=0
negativo=0
positivo=0

while i<=5:
    i=i+1
    n=int(input())
    if n%2==0:
      par=par+1
    else:
      impar=impar+1
    if n>0:
      positivo=positivo+1
    elif n<0:
      negativo=negativo+1
    else:
      zero=0
    
print("{} valor(es) par(es)".format(par))
print("{} valor(es) impar(es)".format(impar))
print("{} valor(es) positivo(s)".format(positivo))
print("{} valor(es) negativo(s)".format(negativo))
