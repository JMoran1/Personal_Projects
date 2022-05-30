# 169. Majority Elements
# https://leetcode.com/problems/majority-element/

def majorityElement(nums) -> int:
    nums.sort()
    return nums[len(nums)//2]


print(majorityElement([2,2,1,1,1,2,2]))