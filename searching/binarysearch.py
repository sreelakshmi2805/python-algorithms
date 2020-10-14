def search(list,key):
	low=0
	high=len(list)-1
	found=False
	while low<=high and not found:
		mid=(low+high)//2
		if key==list[mid]:
			found=True
		elif key>list[mid]:
			low=mid+1
		else:
			high=mid-1
	if found==True:
		print("element is found")
	else:
		print("not found")
list=[34,12,46,90,67,54]
list.sort()
key=int(input("enter the key:"))
search(list,key)
