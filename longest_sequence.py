#To find longest sequence from a list
def longest_sequence(list):
    n = len(list)
    largest = 0
    for sequence in range(n):
        count = 0
        m = list[sequence]
        for j in range(len(m)):
            count=count+1
        if count>largest:
            largest=count
            longest_sequence=m
            index=sequence
    print(longest_sequence,"at the index value",index,",No of element is",largest)
list=[[1,2,7],[2],[4,5,6,9],[3,4]]
longest_sequence(list)