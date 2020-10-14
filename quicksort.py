def pivotposition(nums,first,last):
	pivot=nums[first]
	left=first+1
	right=last
	while True:
		while left<=right and nums[left]<=pivot:
			left=left+1
		while left<=right and nums[left]>=pivot:
			right=right-1
		if right<left:
			break
		else:
			temp=nums[left]
			nums[left]=nums[right]
			nums[right]=temp
	temp = nums[first]
	nums[first] = nums[right]
	nums[right] = temp
	return right
def sort(nums,first,last):
	if first<last:
		p=pivotposition(nums,first,last)
		sort(nums,first,p-1)
		sort(nums,p+1,last)


nums = [11,2,7,9,6,12]
sort(nums,0,len(nums)-1)
print(nums)

















