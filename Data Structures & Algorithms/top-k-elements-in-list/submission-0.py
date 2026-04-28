class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #create dict
        count = {}
        #create first sort
        bucket = [[]for i in range(len(nums)+1)]

        # get values
        for n in nums:
            count[n] = 1+count.get(n, 0)
        
        # add to bucket
        for key, value in count.items():
            bucket[value].append(key)

        # add to res
        res = []
        for i in range(len(bucket)-1, 0, -1):
            for b in bucket[i]:
                res.append(b)

                if len(res) == k:
                    return res


        
        