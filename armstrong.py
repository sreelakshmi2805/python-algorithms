#To check armstrong number
def armstrong(x):
    n=len(str(x))
    sum = 0
    a = 0
    temp=x
    while(temp!=0):
        a=temp%10
        sum=sum+pow(a,n)
        temp=temp//10
    if sum == x:
        print(x,"is an armstrong number")
    else:
        print(x,"is not armstrong number")
x=153
armstrong(x)
