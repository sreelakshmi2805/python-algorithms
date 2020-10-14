def sort(nums):
	for i in range(0,len(nums)-1):
		for j in range(0,len(nums)-1-i):
			if nums[j]>nums[j+1]:
				temp=nums[j]
				nums[j]=nums[j+1]
				nums[j+1]=temp
nums=[7,13,4,11,5,1]
sort(nums)
print(nums)










