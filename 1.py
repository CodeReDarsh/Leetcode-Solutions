class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2: return [0,1]
        
        prevMap = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in prevMap:
                return [prevMap[diff],i]
            else:
                prevMap[nums[i]] = i