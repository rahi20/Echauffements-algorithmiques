#Prob 1 


arr = [1,12,11001, 1232,2,21, 12, 21,23, 213]
n = len(arr)

#memory intensive
arr2 = [None]* n
k = 0
j = n - 1


for i in range(n):
    if arr[i]%2 == 0:
        arr2[k] = arr[i]
        k += 1
    else: 
        arr2[j] = arr[i]
        j -= 1
    i += 1 

#using one array 
head = 0 
tail = n - 1
placeholder = -1

for i in range(n):
    if arr[i]%2 == 0:
        placeholder = arr[head]
        arr[head] = arr[i]
        arr[i] = placeholder 
        head += 1
    else:
        placeholder = arr[tail]
        arr[tail] = arr[i]
        arr[i] = placeholder 
        tail -= 1

    i += 1



print(arr)