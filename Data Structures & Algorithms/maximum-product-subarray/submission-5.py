class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini = maxi = nums[0]
        ret = maxi
        for n in nums[1:]:
            if n < 0:
                mini, maxi = maxi, mini
            maxi = max(n, maxi * n)
            mini = min(n, mini * n)
            ret = max(maxi, ret)
        return ret
