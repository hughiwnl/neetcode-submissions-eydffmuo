class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in numMap:
                return[numMap[diff], index]
            numMap[number] = index
        