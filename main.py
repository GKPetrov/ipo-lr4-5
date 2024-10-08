a = [int(input("Введите элементы списка")) for i in range(1,6)]
count=0
for i in range(len(a)):
    if(a[i]>10):
        count+=1
print(count)