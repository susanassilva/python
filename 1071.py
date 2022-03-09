x = int(input())
y = int(input())
soma = 0

if x%2==0:
    for i in range (x, y, -1):
        if i%2!=0:
            soma+=i
else:
    x = x-1
    for i in range (x, y, -1):
        if i%2!=0:
            soma+=i
            
print(soma)