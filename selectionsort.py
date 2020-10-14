def sort(nums):
	for i in range(0,len(nums)-1):
		min=i
		for j in range(i+1,len(nums)):
			if nums[j]<nums[min]:
				min=j
		temp=nums[i]
		nums[i]=nums[min]
		nums[min]=temp
nums=[7,13,4,11,5,1]
sort(nums)
print(nums)





