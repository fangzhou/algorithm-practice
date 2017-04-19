import sys
import unittest

# DFS Based solution - will time out for large input
class SolutionDFS:
    def books(self, A, B, pos=0):

        L = len(A)
        if L < B:
            return -1
        elif L == B:
            return max(A)
        else:
            curr_min = sys.maxint
            for sep in xrange(1, L):
                sum1 = sum(A[:sep])
                if sum1 > curr_min:
                    continue

                sum2 = self.books(A[sep:], B-1, sep)
                if sum2 != -1:
                    curr_min = min(curr_min, max(sum1, sum2))
            return curr_min

# Binary search solution
class Solution:
    def pages(self, books, numpages):
        curr_sum, student_count = 0, 1
        for book in books:
            curr_sum += book
            if curr_sum > numpages:
                student_count += 1
                curr_sum = book
        return student_count

    def books(self, A, B, debug=False):
        if len(A) < B:
            return -1
        if len(A) == B:
            return max(A)

        low_pagesize, high_pagesize = max(A), sum(A)
        low_pages, high_pages = self.pages(A, low_pagesize), self.pages(A, high_pagesize)
        if debug:
            print "  Start:\n    Low={0} students={1}, High={2} students={3}".format(low_pagesize, low_pages, high_pagesize, high_pages)
            print "    target students={0}\n".format(B)
            
        while low_pagesize < high_pagesize:
            mid = low_pagesize + (high_pagesize - low_pagesize) / 2
            student_count = self.pages(A, mid)
            if debug:
                print "  Mid={0}, Students={1}".format(mid, student_count)
            if student_count <= B:
                high_pagesize = mid
                if debug:
                    print "  (Shrink high)"
            else:
                low_pagesize = mid + 1
                if debug:
                    print "  (Increase low)"

            low_pages, high_pages = self.pages(A, low_pagesize), self.pages(A, high_pagesize)

            if debug:
                print "  Low={0} students={1}, High={2} students={3}\n".format(low_pagesize, low_pages, high_pagesize, high_pages)
            if low_pages == high_pages:
                break

        return low_pagesize


class testSolution(unittest.TestCase):
    def setUp(self):
        self.S = Solution()

    def runTest(self, bookstr, students):
        print
        b = [int(v) for v in bookstr.split()]
        return self.S.books(b, students, debug=True)

    def test_1(self):
        P = "12 34 67 90"
        print "Input: ", P
        R = self.runTest(P, 2)
        print R

    def test_2(self):
        P = "73 58 30 72 44 78 23 9"
        print "Input: ", P
        R = self.runTest(P, 5)
        print R

    def test_3(self):
        P = "23 6 13 70 38 94 20 44 66 34 26 94 63 38 44 90 50 59 23 47 85 17 72 39 47 85"
        print "Input: ", P
        R = self.runTest(P, 7)
        print R

    def test_4(self):
        P = " 97 26 12 67 10 33 79 49 79 21 67 72 93 36 85 45 28 91 94 57 1 53 8 44 68 90 24"
        print "Input: ", P
        R = self.runTest(P, 26)
        print R

    def test_5(self):
        P = "79 83 70 40 23 50 71 29 18 46 99 30"
        print "Input: ", P
        R = self.runTest(P, 1)
        print R
    
if __name__ == "__main__":

    unittest.main()
