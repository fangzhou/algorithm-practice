import unittest

class Solution:

    def min_painters(self, Bm, maxtime):
        painters, timesum = 1, 0
        for boardtime in Bm:
            timesum += boardtime
            if timesum > maxtime:
                painters += 1
                timesum = boardtime
        return painters
    
    # @param painters : integer, number of painters
    # @param speed : integer, time for paint unit length
    # @param B : list of integers, length of boards
    # @return an integer
    def paint(self, painters, speed, B):
        L = len(B)
        Bm = [board*speed for board in B]

        low, high = max(Bm), sum(Bm)
        while low < high:
            mid = low + (high - low)/2
            mid_painters = self.min_painters(Bm, mid)
            if mid_painters <= painters:
                high = mid
            else:
                low = mid+1
        return low

class testSolution(unittest.TestCase):
    def setUp(self):
        self.S = Solution()

    def test_1(self):
        B = [1, 10,3,4,2,6]
        R = self.S.paint(2, 5, B)
        print R

if __name__ == "__main__":
    unittest.main()
