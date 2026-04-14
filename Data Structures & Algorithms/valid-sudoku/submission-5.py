class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        block = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in block[(r//3, c//3)]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                block[(r//3, c//3)].add(board[r][c])
        return True