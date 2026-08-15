class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        ret = nums[0]
        s = nums[0]
        for n in nums[1:]:
            s = max(n, s+n)
            ret = max(ret, s)
        
        prefix = [0]
        p = 0
        mx = float('-inf')
        for n in nums:
            prefix.append(mx)
            p += n
            mx = max(mx, p)

        suffix = []
        s = 0
        mx = float('-inf')
        for n in nums[::-1]:
            suffix.append(mx)
            s += n
            mx = max(s, mx)
        suffix.append(mx)
        suffix = suffix[::-1]
        for i in range(len(nums)):
            ret = max(ret, prefix[i]+suffix[i])
        return ret