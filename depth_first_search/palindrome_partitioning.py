import logging
import sys
import unittest

"""
Problem: For input string s, find all the possible partition combinations that
every partition is a palindrome.
"""

class PalindromePartition(object):
    def is_palin(self, s):
        L = len(s)
        for i in xrange(L/2):
            if s[i] != s[L-i-1]:
                return False
        return True

    def partition(self, s, log=None):
        """
        Recursive DFS solution: Using DFS to search for all possible break
        points which can partition string into palindromes. Only continue
        recursion if the first part is palindrome.

        Args:
          s: remaining unpartitioned part of input string

        """
        L = len(s)
        results = []

        if log is None:
            log = logging.getLogger(sys._getframe().f_code.co_name)
            log.setLevel(logging.DEBUG)

        def match_palin(s, prefix, results):
            """
            helper funtion for recursive DFS
            """
            L = len(s)
            log.debug(" "*len(prefix) + "remaining string: {0}, prefix: {1}".format(s, prefix))
            if L == 0:
                results.append(prefix)
                return
            for i in xrange(1, L+1):
                _prefix = s[:i]
                if self.is_palin(_prefix):
                    log.debug(" "*len(prefix) + "Found palindrome: " + _prefix)
                    match_palin(s[i:], prefix + [_prefix], results)

        match_palin(s, [], results)
        return results

class testPalindromePartition(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("testPalindromePartition")
        self.S = PalindromePartition()

    def test_palinpart_1(self):
        print "Test 1:",
        s = "aab"
        print "Input:", s
        results = self.S.partition(s)
        print results

    def test_palinpart_1_2(self):
        print "Test 1.2:",
        s = "accac"
        print "Input:", s
        results = self.S.partition(s)
        print results

    def test_palinpart_2(self):
        print "Test 2:",
        s = "ababbbabbaba"
        print "Input:", s
        results = self.S.partition(s, self.logger)
        print results

if __name__ == "__main__":
    unittest.main()
