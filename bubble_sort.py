

arr = [ 10, 1, -1] # [1 10 -1] [-1 10 1] [-1 1 10]

size = len(arr) # 3
# n * (n-1) = n2-n n*
for i in range(size): # 0, 1, 2
    for j in range(i, size): # 0, 1, 2, 1, 2, 2
        print(arr[i], arr[j])
        # print("arr[i] is {0} and arr[j] is {1}".format(arr[i], arr[j]))
        if arr[i] > arr[j]: 
            arr[i], arr[j] = arr[j], arr[i]

print(arr)