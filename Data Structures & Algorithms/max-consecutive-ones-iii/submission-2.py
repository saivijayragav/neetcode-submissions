class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        z = 0
        ret = 0
        while r<len(nums):
            if nums[r] == 0:
                z += 1
            while l <= r and z > k:
                if nums[l] == 0:
                    z -= 1
                l += 1
            ret = max(ret, r-l+1)
            r += 1
        return ret