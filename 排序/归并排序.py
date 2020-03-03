def merge(nums1, nums2, nums):
    l1, l2 = len(nums1), len(nums2)
    i, j = 0, 0

    while i < l1 and j < l2:
        if nums1[i] < nums2[j]:
            nums[i+j] = nums1[i]
            i += 1
        else:
            nums[i+j] = nums2[j]
            j += 1

    while i < l1:
        nums[i+j] = nums1[i]
        i += 1
    while j < l2:
        nums[i+j] = nums2[j]
        j += 1


def merge_sort(nums):
    n = len(nums)
    if n < 2:
        return

    mid = n // 2
    nums1 = nums[0: mid]
    nums2 = nums[mid: n]

    merge_sort(nums1)
    merge_sort(nums2)
    merge(nums1, nums2, nums)


nums = [43,5,8,41,3,48,4,1,3,]
merge_sort(nums)
print(nums)