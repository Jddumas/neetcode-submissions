class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #l, m, r
        #l>n<m, search left
        #m<n<r
        l = 0
        r = len(nums)-1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # if left portion is sorted
            if nums[l] <= nums[mid]:
                #if its not in there
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1

                # if it is
                else:
                    r = mid - 1

            # if right portion is sorted
            else:
                # if its not in there
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                # if it is
                else:
                    l = mid + 1
        return -1

        