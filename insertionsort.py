def insertion_sort(nums):
	for i in range(1,len(nums)):
		temp=nums[i]
		j=i
		while temp<nums[j-1] and j>0:
			nums[j]=nums[j-1]
			j=j-1
		nums[j]=temp
nums=[5,1,65,2,7,6,9,100,67,98,34]
insertion_sort(nums)
print(nums)


