
n = int(input())

arr = [0]*1000

for i in range(0,n):
    arr[i] = int(input())

for i in range (0,n):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            tmp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = tmp

for i in range(0,n):
    print(arr[i] , end=" ")


