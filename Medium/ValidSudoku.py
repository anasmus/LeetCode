class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        # validate rows
        for row in range(9):
            seen.clear()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # validate cols
        for col in range(9):
            seen.clear()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])

        # validate boxes
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                seen.clear()
                for i in range(3):
                    for j in range(3):
                        if board[row + i][col + j] == ".":
                            continue
                        if board[row + i][col + j] in seen:
                            return False
                        seen.add(board[row + i][col + j])

        return True
