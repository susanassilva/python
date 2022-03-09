n = int(input())
dentro = 0
out = 0
for i in range (n):
    x = int(input())

    if x >= 10 and x <= 20 :
        dentro = dentro + 1
    else:
        out = out + 1
      
print('{} in'.format(dentro))
print('{} out'.format(out))