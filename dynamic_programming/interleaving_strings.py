import unittest

"""
Problem: Given 3 strings A, B and C, determine, if C can be produced by
interleaving A and B
"""

class DFSSolution(object):
    """
    DFS based solution + Memoization
    """
    def __init__(self):
        self.M = None

    def dfs(self, Ar, Br, Cr):
        """
        Args:
          Ar, Br, Cr: remaining part of A, B, C
        """
        LAr, LBr = len(Ar), len(Br)
        LCr = len(Cr)

        # Memoization array is only used for stopping search
        if self.M[LAr][LBr][LCr] == False:
            return self.M[LAr][LBr][LCr]
        else:
            if LCr != LAr + LBr:
                # Stop early: if length not match
                return False
            if LCr == 0:
                # Reached end of string
                return True

            anymatch = False
            rA, rB = None, None
            if LAr > 0 and Ar[0] == Cr[0]:
	            rA = self.dfs(Ar[1:], Br, Cr[1:])
            if LBr > 0 and Br[0] == Cr[0]:
	            rB = self.dfs(Ar, Br[1:], Cr[1:])
            anymatch = (rA == 1) or (rB == 1)
            if not anymatch:
                self.M[LAr][LBr][LCr] = False
                return False
            else:
                return True

    def isInterleave(self, A, B, C):
        self.M = [[[None for _ in xrange(len(C)+1)] for _ in xrange(len(B)+1)] for _ in xrange(len(A)+1)]
        return self.dfs(A, B, C)

class DPSolution(object):
    def isInterleave(self, A, B, C):
        l1, l2 = len(A), len(B)
        l3 = len(C)
        if l1+l2 != l3:
            return False

        F = [[False for _ in xrange(l2+1)] for _ in xrange(l1+1)]

        # Initialize first column and first row: only true if prefix matches between A or B with C
        for i in xrange(l1+1):
            F[i][0] = (A[0:i] == C[0:i])

        for i in xrange(l2+1):
            F[0][i] = (B[0:i] == C[0:i])

        """
        2D Dynamic programming on string A and B:
        F[i][j] i: position in A, j: position in B
                =    F[i-1][j] and A[i-1] == C[i+j-1] (last character in A is same with last character in C)
                  or F[i][j-1] and B[j-1] == C[i+j-1] (last character in B is same with last character in C)
        """

        for i in xrange(1, l1+1):
            for j in xrange(1, l2+1):
                F[i][j] = (F[i-1][j] and A[i-1] == C[i+j-1]) or (F[i][j-1] and B[j-1] == C[i+j-1])

        return F[l1][l2]

class testSolution(unittest.TestCase):
    def setUp(self):
        self.DFS = DFSSolution()
        self.DP = DPSolution()

    def test_1(self):
        A, B = "aabcc", "dbbca"
        C = "aadbbcbcac"
        print "Test 1"
        print "A=\"{0}\", B=\"{1}\", C=\"{2}\"".format(A, B, C)

        DFS_result = self.DFS.isInterleave(A, B, C)
        DP_result = self.DP.isInterleave(A, B, C)
        print "DFS Result: {0}, DP Result: {1}, Equal: {2}".format(DFS_result, DP_result, DFS_result == DP_result)

    def test_1_neg(self):
        A, B = "aabcc", "dbbca"
        C = "aadbbbaccc"
        print "Test 1 Negatice"
        print "A=\"{0}\", B=\"{1}\", C=\"{2}\"".format(A, B, C)

        DFS_result = self.DFS.isInterleave(A, B, C)
        DP_result = self.DP.isInterleave(A, B, C)
        print "DFS Result: {0}, DP Result: {1}, Equal: {2}".format(DFS_result, DP_result, DFS_result == DP_result)

    def test_2(self):
        A, B = "cacccaa", "acccaacabbbab"
        C = "accccaaaccccabbaabab"
        print "Test 2"
        print "A=\"{0}\", B=\"{1}\", C=\"{2}\"".format(A, B, C)

        DFS_result = self.DFS.isInterleave(A, B, C)
        DP_result = self.DP.isInterleave(A, B, C)
        print "DFS Result: {0}, DP Result: {1}, Equal: {2}".format(DFS_result, DP_result, DFS_result == DP_result)

    def test_3(self):
        A, B = "abaaacbacaab", "bcccababccc"
        C = "bcccabaaaaabccaccbacabb"
        print "Test 3"
        print "A=\"{0}\", B=\"{1}\", C=\"{2}\"".format(A, B, C)

        DFS_result = self.DFS.isInterleave(A, B, C)
        DP_result = self.DP.isInterleave(A, B, C)
        print "DFS Result: {0}, DP Result: {1}, Equal: {2}".format(DFS_result, DP_result, DFS_result == DP_result)


if __name__ == "__main__":
    unittest.main()
