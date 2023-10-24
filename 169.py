class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Majority Vote Algorithm O(n) time O(1) space
        count, max = 0,0
        for n in nums:
            if count == 0: max, count = n,1
            elif n == max: count+=1
            else: count-=1
        return max

        """
        alternate solution O(n) space and time:

        map,max = {},nums[0]
        for n in nums:
            if n in map:
                map[n]+=1
            max = n if map[n] > map[max] else max
        return max
        """