def sort(nums):
    
    for i in range(len(nums)-1) :
        minpos = i
        for j in range(i, len(nums)) :
            if nums[j] < nums[minpos] :
                minpos = j
            
        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

nums = [5, 62, 78, 2, 6, 49]
sort(nums)

print(nums)
