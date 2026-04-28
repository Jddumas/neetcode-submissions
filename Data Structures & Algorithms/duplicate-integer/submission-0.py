class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # understand
        # arr nums, return true of any value more than once, else false
        # plan = hashmap, put the value at the hash # and then you can check
        # this will be n time and n space
        hashmap = {}
        for num in nums:
            # check if num at hashmap, if not add it 
            if num in hashmap:
                return True
            hashmap[num] = num

        return False

        