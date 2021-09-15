idade=int(input())

A=idade//365
idade=idade-A*365

B=idade//30
idade=idade-B*30


C=idade
print("%d ano(s)"%A)
print("%d mes(es)"%B)
print("%d dia(s)"%C)