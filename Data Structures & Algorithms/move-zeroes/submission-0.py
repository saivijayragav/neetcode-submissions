class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[r], nums[z] = nums[z], nums[r]
                z += 1
        
                

