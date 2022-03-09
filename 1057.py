X = int(input())
Y = int(input())

total=0

if X%2==0:
  for i in range (X, Y, -1):
    if i%2!=0:
      total+=i

else:
  X=X-1
  for i in range (X, Y, -1):
    if i%2!=0:
      total+=i
  

print(total)
  

