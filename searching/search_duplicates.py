#search the key element in the list and to print index value of duplicate key element

def search(list,key):
	list1=[]
	flag=False
	for i in range(len(list)):
		if key==list[i]:
			flag=True
			list1.append(i)
	if flag==True:
		print("element is found at index:")
		for i in list1:
			print(i)
	else:
		print("element is not found")
		
		
	
list=[23,45,6,43,78,15,6,5]
key=int(input("enter the key element"))
search(list,key)
