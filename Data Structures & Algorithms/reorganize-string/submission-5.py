class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s) #dictionary of counts, with key and value
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)
        prev = None
        res = ""

        while maxHeap or prev:
            if prev and not maxHeap:
                return ""

            #pop from heap
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1
            
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            
            if cnt !=0:
                prev = [cnt,char]

            # if prev add to heap and set prev to none
            # if count is not zero, add to prev

        return res
        