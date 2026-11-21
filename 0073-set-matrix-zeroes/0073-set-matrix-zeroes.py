class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zr = []
        zc = []
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    zr.append(i)
                    zc.append(j)
        
        for i in zr:
            matrix[i] = [0] * m

        for j in zc:
            for k in range(n):
                matrix[k][j] = 0