def sSort(nums):
    for i in range(len(nums)):
        last = len(nums)-i-1
        maxIndex = getMaxIndex(nums, 0, last)
        nums[last], nums[maxIndex] = nums[maxIndex], nums[last]
    return nums
def getMaxIndex(nums, startidx, lastidx):
    max = startidx
    for i in range(startidx, lastidx+1):
        if nums[i] > nums[max]: max=i
    return max

nums=[1,5,97,2,4, 98]
print(sSort(nums))