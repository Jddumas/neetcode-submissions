class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # go through each index
        # target - num = pair
        # search if pair is in the dict, if not add
        # when you find it add both
        pairDict = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in pairDict:
                return [pairDict[pair], i]
            else:
                pairDict[nums[i]] = i
        