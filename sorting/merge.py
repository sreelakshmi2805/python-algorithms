def mergesort(nums):
	if len(nums)>1:
		mid=len(nums)//2
		left_nums=nums[:mid]
		right_nums=nums[mid:]
		mergesort(left_nums)
		mergesort(right_nums)
		i=0
		j=0
		k=0
		while i<len(left_nums) and j<len(right_nums):
			if left_nums[i]<right_nums[j]:
				nums[k]=left_nums[i]
				i=i+1
				k=k+1
			else:
				nums[k]=right_nums[j]
				j=j+1
				k=k+1
		while i<len(left_nums):
			nums[k]=left_nums
			i=i+1
			k=k+1
		while j<len(right_nums):
			nums[k]=right_nums
			j=j+1
			k=k+1
nums=[13,45,65,21,11,70,34]
mergesort(nums)
print(nums)













