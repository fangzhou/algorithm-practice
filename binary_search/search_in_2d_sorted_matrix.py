import unittest

"""
Problem: Given a matrix which all rows and columns are sorted in ascending
order, search for a value in this matrix.
"""

class Solution(object):
    def printMatrix(self, m, x1, y1, x2, y2):
        """
        For debug usage: Print a submatrix
        """
        for i in xrange(x1, x2+1):
            print "[",
            for j in xrange(y1, y2+1):
                print m[i][j],
            print "]"

    def shrink(self, m, t, x1, y1, x2, y2):
        """
        Since all rows and columns in matrix is sorted, this helper function
        will shrink the matrix search range.

        Args:
          x1: row index for upper left corner of the search region
          y1: column index for upper left corner of the search region
          x2: row index for lower right corner of the search region
          y2: column index for lower right corner of the search region
          m: input matrix
          t: target number

        Return:
          (rx1, ry1, rx2, ry2): Coordinates for the new narrow downed region
        """
        rows, cols = x2-x1+1, y2-y1+1
        rx1 = x1
        while rx1 < x2 and m[rx1][y2] < t:
            rx1 += 1
        if m[rx1][y2] == t:
            return rx1, y2, rx1, y2

        rx2 = x2
        while rx2 > x1 and m[rx2][y1] > t:
            rx2 -= 1
        if m[rx2][y1] == t:
            return rx2, y1, rx2, y1

        ry1 = y1
        while ry1 < y2 and m[x2][ry1] < t:
            ry1 += 1
        if m[x2][ry1] == t:
            return x2, ry1, x2, ry1

        ry2 = y2
        while ry2 > y1 and m[x1][ry2] > t:
            ry2 -= 1
        if m[x1][ry2] == t:
            return x1, ry2, x1, ry2

        return rx1, ry1, rx2, ry2

    def searchMatrix(self, matrix, target):
        """
        Args:
          matrix: List[List[int]]
          target: int

        Return: bool indicating if target exists in matrix or not
        """
        rows, cols = len(matrix), len(matrix[0])
        x1, y1 = 0, 0
        x2, y2 = rows-1, cols-1
        print "Start:"
        print x1, y1, x2, y2
        self.printMatrix(matrix, x1, y1, x2, y2)
        while x1 != x2 and y1 != y2:
            x1, y1, x2, y2 = self.shrink(matrix, target, x1, y1, x2, y2)
            print
            print x1, y1, x2, y2
            self.printMatrix(matrix, x1, y1, x2, y2)
            if x1 > x2 or y1 > y2:
                return False

        for i in xrange(x1, x2+1):
            for j in xrange(y1, y2+1):
                if matrix[i][j] == target:
                    return True
        return False

    def searchDuplicates(self, matrix, target):
        """
        Return the number of occurrence of target in matrix
        Integers in each row are sorted from left to right.
        Integers in each column are sorted from up to bottom.
        LIMITATION: No duplicate integers in each row or column.
        """
        if matrix == [] or matrix[0] == []:
            return 0

        row, column = len(matrix), len(matrix[0])
        count = 0
        i, j = row - 1, 0
        while i >= 0 and j < column:
            print "i,j = ",i,",",j
            if matrix[i][j] == target:
                count += 1
                i -= 1
                j += 1
            elif matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1
        return count

class testSolution(unittest.TestCase):
    def setUp(self):
        self.S = Solution()
        self.Sd = self.S.searchDuplicates
        self.m1 = [[1,  4,  7, 11, 15],
                   [2,  5,  8, 12, 19],
                   [3,  6,  9, 16, 22],
                   [10,13, 14, 17, 24],
                   [18,21, 23, 26, 30]]

    def test_1(self):
        self.S.searchMatrix(self.m1, 14)
        print "====="
        self.S.searchMatrix(self.m1, 15)
        print "====="
        self.S.searchMatrix(self.m1, 3)
        print "====="
        self.S.searchMatrix(self.m1, 24)
        print "====="
        self.S.searchMatrix(self.m1, 25)

    def test_2(self):
        _m = [[1,1]]
        self.S.searchMatrix(_m, 0)

    def test_3(self):
        _m = [[1,4], [2,5]]
        self.S.searchMatrix(_m, 0)


    def test_4(self):
        # Duplicated numbers
        _m = [[5,6,9],[9,10,11],[11,14,18]]
        self.S.searchMatrix(_m, 9)

    def test_d_1(self):
        print "====="
        print "test searchDuplicates 1"
        _m = [[1, 3, 5, 7],
              [2, 4, 7, 8],
              [3, 5, 9, 10]]
        r = self.Sd(_m, 3)
        print r

    def test_d_2(self):
        print "====="
        print "test searchDuplicates 2"
        _m = [[1, 3, 4, 5, 9],
              [2, 4, 7, 8, 10],
              [3, 5, 9, 11, 12]]
        r = self.Sd(_m, 4)
        print r

if __name__ == "__main__":
    unittest.main()
