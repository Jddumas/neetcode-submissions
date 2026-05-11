class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final_arr = []
        nums.sort()
        # 3 pointer
        for i, n in enumerate(nums):
            #move up if i is the same
            if i > 0 and n == nums[i-1]:
                    continue

            # now match with l + r
            l = i + 1
            r = len(nums) - 1
            while l < r:
                totalsum = n + nums[l] + nums[r]
                
                if totalsum < 0:
                    l += 1

                elif totalsum > 0:
                    r -= 1

                #found
                else:
                    final_arr.append([n, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1 
        return final_arr
