#To reverse an array
def reverse(arr):
    m = len(arr)
    start=0
    end=m-1
    while(start<end):
        temp=arr[start]
        arr[start]=arr[end]
        arr[end]=temp
        start=start+1
        end=end-1
    return arr
arr=[7,8,9,6,4,5,1,3,2]
print(reverse(arr))








