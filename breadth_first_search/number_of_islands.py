import unittest

"""
Problem: Given a matrix only have 0 and 1 values, consider 0 as ocean and 1 as land.
Also adjacent 1 cells in matrix can be considered as same island, find out how
many islands totally in given matrix.
"""

class NumOfIslands:
    def __init__(self):
        self.G = None
        self.rows = 0
        self.cols = 0
        self.island_count = 0

    def neighbors(self, i, j):
        """
        Given a coordinate, return all adjancent cell's coordinates.
        We only consider up, down, left, right as adjancent.
        """
        def _valid(x, y):
            return (x >= 0 and x < self.rows) and (y >= 0 and y < self.cols) and (self.G[x][y] == 1)
        NV = [(-1,0), (0,1), (1,0), (0,-1)]

        if self.G[i][j] == 1:
            n = [(i+d[0], j+d[1]) for d in NV if _valid(i+d[0], j+d[1])]
            return n
        else:
            return []

    def bfs_expand(self, i, j):
        """
        From a given cell which is land, expand using BFS to all its neighbours
        to connect all land cells into a single island. Visited cells are marked 
        back to 0
        """
        if self.G[i][j] == 1:
            q = []
            q.append((i,j))
            while len(q) > 0:
                cc = q.pop(0)
                ns = self.neighbors(cc[0], cc[1])
                q = q + ns
                self.G[cc[0]][cc[1]] = 0
            self.island_count += 1

    def numIslands(self, grid):
        """
        For each 1 cell in matrix, call bfs_expand() to connect all adjancent 
        1 cell into an island, count the island counts.
        """
        self.G = grid
        self.rows = len(grid)
        if self.rows == 0:
            return 0
        self.cols = len(grid[0])
        self.island_count = 0

        for i in xrange(self.rows):
            for j in xrange(self.cols):
                if self.G[i][j] == 1:
                    self.bfs_expand(i, j)

        return self.island_count

class testNumOfIslands(unittest.TestCase):
    def setUp(self):
        self.findIslands = NumOfIslands()

    def test_1(self):
        grid = [[1, 1, 0, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1]]
        result = self.findIslands.numIslands(grid)
        print result

    def test_2(self):
        grid = [[1,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,0],[0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,0,1,0,1,0],[0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,1,0,0,1],[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,1,0,1],[0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0],[0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1],[0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0],[1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0],[0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0],[1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1],[0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0],[0,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0],[1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,0,1,1],[1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0],[0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,1,0,0],[0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1],[0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0]]
        result = self.findIslands.numIslands(grid)
        print result
        
if __name__ == "__main__":
    unittest.main()
