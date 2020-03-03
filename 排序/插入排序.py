def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
            else:
                break

nums = [43,5,8,41,3,48,4,1,3,0]
insert_sort(nums)
print(nums)
