class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for a in range(len(nums) - 2):
            if nums[a] > 0:
                break

            if a > 0 and nums[a] == nums[a - 1]:
                continue

            l = a + 1
            r = len(nums) - 1
            while l < r:
                threeSum = nums[a] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res
