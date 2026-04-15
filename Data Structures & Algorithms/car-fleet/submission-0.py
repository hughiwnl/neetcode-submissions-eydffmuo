class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0
        stack = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            stack.append((position[i], time))

        stack.sort(reverse=True)
        slowest_time = 0

        for pos, time in stack:
            if time > slowest_time:
                res += 1
                slowest_time = time
        
        return res