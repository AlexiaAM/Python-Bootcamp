#saber cuantos numeros diferentes hay

n = int(input())

cont = 0
arr = [0]*1000
bucket = [0]*1000

for i in range(0,n):
    arr[i] = int(input())
    if bucket[arr[i]]>=1:
        bucket[arr[i]]+=1
    else:
        bucket[arr[i]]=1

for i in range(0,100):
    if bucket[i]>=1:
        cont+=1
print(cont)
