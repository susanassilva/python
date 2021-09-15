for item in [3,4,5,6,7,8,9]:
    print(item, end=" ")
print()

num = int(input("Digite valor inteiro e positivo:"))
fat = 1
for i in range(1,num+1):
    fat = fat*i
print("O fatorial de", num, "=", fat)