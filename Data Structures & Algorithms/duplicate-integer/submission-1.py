class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # understand
        # true if num more than once
        # false if once
        # use hashmap for n time and n space
        hashmap = {}
        for num in nums:
            # if the key is in the hashmap
            if num in hashmap:
                return True
            else:
                hashmap[num] = 0
        return False


        