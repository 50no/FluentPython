def shell_sort(nums):
    n = len(nums)

    gap = 1
    while gap < n:
        gap = gap * 2 + 1
    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i - gap
            while j >= 0 and nums[j] > temp:
                nums[j + gap] = nums[j]
                j -= gap
            nums[j + gap] = temp
        gap = gap // 2


nums = [43,5,8,41,3,48,4,1,3,]
shell_sort(nums)
print(nums)
