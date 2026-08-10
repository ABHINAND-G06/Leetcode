class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        colmap=defaultdict(set)
        blockmap=defaultdict(set)
        rowmap=defaultdict(set)
        for i in range(9):
            for j in range(9):
                cell=board[i][j]
                if cell=='.':
                    continue
                if cell in rowmap[i]:
                    return False
                if cell in colmap[j]:
                    return False
                if cell in blockmap[(i//3,j//3)]:
                    return False
                colmap[j].add(cell)
                rowmap[i].add(cell)
                blockmap[(i//3,j//3)].add(cell)
        return True