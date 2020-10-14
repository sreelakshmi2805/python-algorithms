#To find largest and second largest elements in an array
def largest(arr):
    large=arr[0]
    sec_large=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>large:
            sec_large=large
            large=arr[i]
        elif arr[i]>sec_large:
            sec_large=arr[i]
    print("largest element is",large)
    print("second largest element is",sec_large)


arr=[34,76,90,89,56,98]
largest(arr)

