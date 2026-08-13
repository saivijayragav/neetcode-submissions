class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ret = []
        for p in range(len(nums)):
            if p > 0 and nums[p-1] == nums[p]:
                continue
            for q in range(p+1, len(nums)):
                if q > p+1 and nums[q-1] == nums[q]:
                    continue
                l, r = q+1, len(nums)-1
                t = target - (nums[p] + nums[q])
                while l<r:
                    s = nums[l] + nums[r]
                    if s > t:
                        r -= 1
                    elif s < t:
                        l += 1
                    else:
                        ret.append([nums[p], nums[q], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return ret