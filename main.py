# def twoSum(nums, target):
#     result = []
#     for i in nums:
#         for j in nums[nums.index(i) + 1:]:
#             if i + j == target:
#                 result.append(nums.index(i))
#                 result.append(nums.index(j))
#                 break
#     return result
def twoSum(nums, target):
    result = []
    for x in nums:
        y = target - x
        if y in nums and nums.index(x) != nums.index(y)
            result.append(nums.index(x))
            result.append(nums.index(y))
            break
    return result
#check1 = twoSum([1, 2, 3], 4)
#print(check1)
#check2 = twoSum([3, 2, 4], 6)
#print(check2)
#check3 = twoSum([2, 7, 11, 15], 9)
#print(check3)
check4 = twoSum([3, 3], 6)
print(check4)