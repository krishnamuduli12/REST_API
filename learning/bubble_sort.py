def bubble_sort(nums):
    for i in range(len(nums)-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    

def bubble_sort1(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0, n-i-1 ):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                

nums = [5,12,34,16,30,9,26]

print("before sorting the list: ", nums)

#bubble_sort(nums)
bubble_sort1(nums)

print("After sorting the list: ", nums)

