class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input: int array of nums, int k
        # output: # of most frequent elements, kth amount
        # match: hashmap for counting, min heap for listing. iterate backwards over heap
        minheap = [[] for i in range(len(nums)+1)]
        hashmap = {}
        res = []

        for num in nums:
            #add 1 to hashmap, key = int, value = cunt
            hashmap[num] = 1 + hashmap.get(num, 0)

        # add to minheap list
        for num, c in hashmap.items():
            minheap[c].append(num)

        # pop off minheap in reverse order
        for i in range(len(nums), 0, -1):
            #pop off each one
            for item in minheap[i]:
                res.append(item)
                if len(res) == k:
                    return res




