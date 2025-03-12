def second_Element(arr):
    max=-float('inf')
    for item in arr:
        if item>max:
            max=item
    
    second_max=-float('inf')
    for item in arr:
        if item>second_max and item<max:
            second_max=item                        
    
    smallest=float('inf')
    for item in arr:
        if item<smallest:
            smallest=item

    second_smallest=float('inf')
    for item in arr:
        if item<second_smallest and item>smallest:
            second_smallest=item
            
    return [second_max,second_smallest]

arr=[5,18,56,78,23,1,9]
second_max,second_smallest=second_Element(arr)
print("Highest number is:",max(arr))
print("second highest number is:",second_max)
print("smallest number is:",min(arr))
print("second smallest number is:",second_smallest)
