class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visited = sorted(zip(timestamp, username, website))

        userList = defaultdict(list)
        for t, u, w in visited:
            userList[u].append(w)

        count = defaultdict(int)
        for u in userList:
            for pattern in set(combinations(userList[u], 3)):
                count[pattern] += 1
        return list(min(count, key=lambda p: (-count[p], p )))

        
