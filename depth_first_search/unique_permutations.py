
import logging
import sys
import unittest

"""
Problem: Given a list of integers, generate all unique permutation series from
these integers. The input list may have duplicated numbers.
"""

def permuter(results, nums, prefix, log):
    """
    DFS based permuter:

    Args:
    results: result output list
    nums: sorted input array
    prefix: generated prefix for permutation string, notice we are storing
    index for numbers in input, not the numbers

    Returns: None, results being appended to results list
    """

    if len(prefix) == len(nums):
        # All numbers in input have been used, convern index to number
        # and add to result
        results.append([nums[p] for p in prefix])
        return
    else:
        for i in xrange(len(nums)):
            if i in prefix:
                # if number at position i already used
                continue
            elif i > 0 and nums[i] == nums[i-1] and i-1 not in prefix:
                # for duplicated number, always picking the first occurrence
                continue
            else:
                # Recursively adding new results by appending the prefix
                log.debug(len(prefix)*" " + str(prefix))
                log.debug(len(prefix)*" " + "current index: {0}:{1}, prev: "
                          "{2}:{3}".format(i, nums[i], i-1, nums[i-1]))
                permuter(results, nums, prefix + [i], log)


def permute(nums, log=None):
    if log is None:
        log = logging.getLogger(sys._getframe().f_code.co_name)
        log.setLevel(logging.DEBUG)

    results = []
    sorted_nums = sorted(nums)
    permuter(results, sorted_nums, [], log)
    return results

class testPermuter(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("ShortestSubarray")

    def test_1(self):
        A = [1,1,2]
        print "Test 1:\nInput: {0}".format(str(A))
        result = permute(A)
        print "Result: {0}".format(str(result))

    def test_2(self):
        A = [-1,2,-1,2,1,-1,2,1]
        print "Test 2:\nInput: {0}".format(str(A))
        result = permute(A, self.logger)
        print "Result: {0}".format(str(result))

    def test_3(self):
        A = [2,2,3,3,3]
        print "Test 3:\nInput: {0}".format(str(A))
        result = permute(A, self.logger)
        print "Result: {0}".format(str(result))


if __name__ == "__main__":
    unittest.main()
