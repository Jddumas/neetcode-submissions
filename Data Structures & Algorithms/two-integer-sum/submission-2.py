class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # understand
        # input: arr of ints
        # input: 1 integer
        # output: index i & j
        # condition: index i and j = target and i != j
        # match, hashmap. 
        # check if the i has a match to j
        # if not add it
        # check map[i] = target=j
        dict1 = {}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        

        