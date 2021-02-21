def sort(nums):
    for i in range(1, len(nums)):
        anchor = nums[i]
        j = i - 1
        while j>=0 and anchor < nums[j]:
            nums[j+1] = nums[j]
            j = j - 1
            nums[j+1] = anchor
        
nums = [12, 2, 89, 105, 63, 4, 57, 99];
sort(nums)

print(nums)