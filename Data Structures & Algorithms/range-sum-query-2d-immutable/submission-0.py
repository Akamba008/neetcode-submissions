class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLUMNS = len(matrix[0])
        self.sum_mat = [[0] * (COLUMNS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLUMNS):
                prefix += matrix[r][c]
                above = self.sum_mat[r][c + 1]
                self.sum_mat[r+1][c+1] = prefix + above

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, row2, col1, col2 = row1 + 1, row2 + 1, col1 + 1, col2 + 1

        bottom_right = self.sum_mat[row2][col2]
        above = self.sum_mat[row1 - 1][col2]
        left = self.sum_mat[row2][col1 - 1]
        top_left = self.sum_mat[row1 - 1][col1 - 1]

        return bottom_right - above - left + top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)