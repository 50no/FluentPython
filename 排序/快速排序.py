def quick_sort(nums):

    def partition(nums, left, right):
        key = left

        while left < right:
            while left < right and nums[right] >= nums[key]:
                right -= 1
            while left < right and nums[left] <= nums[key]:
                left += 1
            nums[left], nums[right] = nums[right], nums[left]

        nums[left], nums[key] = nums[key], nums[left]

        return left



    def real_sort(nums, left, right):
        if left >= right:
            return

        mid = partition(nums, left, right)
        real_sort(nums, left, mid-1)
        real_sort(nums, mid+1, right)


    n = len(nums)
    real_sort(nums, 0, n-1)

nums = [43,5,8,41,3,48,4,1,3,]
quick_sort(nums)
print(nums)