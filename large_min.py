#To find the largest and smallest element in an array
def large_small(arr):
    large=arr[0]
    small=arr[0]
    for i in range(len(arr)):
        if arr[i]>large:
            large=arr[i]
        elif arr[i]<small:
            small=arr[i]
    print("largest element is", large)
    print("smallest element is", small)
    
arr=[34,76,90,89,56,98]
large_small(arr)

