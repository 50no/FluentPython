def selection_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        min_index = i
        for j in range(i, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

nums = [43,5,8,41,3,48,4,1,3,]
selection_sort(nums)
print(nums)
