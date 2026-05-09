class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # input: arr of numbers, sorted in increasing order
        # output: index of two numbers [i, j] that add to target, i<j
        # 2 pointers. if its less than target, move right. if its greater, move left

        l = 0
        r = len(numbers)-1

        while l<r:
            sum1 = numbers[l] + numbers[r]

            if sum1 == target:
                return [l+1, r+1]
            
            if sum1 > target:
                r -= 1
            elif sum1 < target:
                l +=1
        

        