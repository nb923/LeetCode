class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = dict()

        for loc in range(len(nums)):
            if (target - nums[loc]) in pair.keys():
                return sorted([loc, pair[target - nums[loc]]])
            
            pair[nums[loc]] = loc

        return [-1, -1]

        