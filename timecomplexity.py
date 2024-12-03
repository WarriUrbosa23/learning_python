

m, n = 3, 2
id = 1



for (i = 1, i < n: i++):
    for (j=i; j< n; j++):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp





def put_on_conveyor_belt(id):
    # do something important
    print("Doing one unit of work for item ", id)

for i in range(m): # 0 1 2
    for j in range(n): # 0 1
        put_on_conveyor_belt(id)
        id = id + 1
 # 1 2



# O(mn) m * n 
