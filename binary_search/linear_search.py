def binary_search(arr, element):
    """
    @arr: A list of elements sorted in ascending order
    @element: The element to search for
    @return: The index of the element if present in arr. -1 if not present
    """
    ## Write your code here
    for r in range(0, len(arr)):
        if element == arr[r]:
            print("Dein nummer ist in Platz", r)
            return r
    print("Dein nummer ist nicht hier. Es tut mir leid.")
    return -1
        

assert(binary_search([0,1,2,3,4,5], 3) == 3)
assert(binary_search([10, 19, 24, 28, 29, 100], 100) == 5)
assert(binary_search([1], 10) == -1)