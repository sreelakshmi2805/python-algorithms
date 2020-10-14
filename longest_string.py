# To find largest string in list
def longest(list):
    length=0
    for word in list:
        if len(word)>length:
            length=len(word)
    return word,length
list=['one','twenty','four','seven']
print("largest string is",longest(list))