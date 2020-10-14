def search(list,key):
	for i in range(len(list)):
		if key==list[i]:
			print("element is found at index",i)
			break
	else:
		print("element is not found")
list=[23,45,6,43,78,15]
key=int(input("enter the key element"))
search(list,key)