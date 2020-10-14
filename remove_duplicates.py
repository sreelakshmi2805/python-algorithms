#To remove duplicates from sorted array

def remove_duplicates(list):
    n=len(list)
    if(n==0 or n==1):
        return list
    pivot=0
    for value in range(0,n-1):
        if(list[value])!=list[value+1]:
            list[pivot]=list[value]
            pivot=pivot+1
    list[pivot]=list[n-1]
    return list[0:pivot+1]


list=[2,2,3,3,3,4,4,5,5,5,5,6,6]
print(remove_duplicates(list))
