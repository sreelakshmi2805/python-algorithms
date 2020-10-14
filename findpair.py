#To find if there exist a pair of elements in an unsorted array with difference m

def pair(arr,m):
    first = 0
    second= 1
    arr.sort()
    length=len(arr)
    while first< length and second<length:
        if arr[second]-arr[first]==m and first!=second:
            print("pair found", arr[first], ",", arr[second])
            return True
        elif arr[second]-arr[first]<m:
            second+=1
        else:
            first+=1
    print("no pair found")
    return False

arr=[45,20,70,8,10]
m= 60
pair(arr,m)

