N=int(input())
conv=3600
hora=(N//conv)
min=(N-(conv*hora))//60
seg=(N-(conv*hora)-(min*60))


print("%d:%d:%d" %(hora,min,seg))