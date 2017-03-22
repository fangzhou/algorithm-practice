"""
Problem: Given a positive interger array (nums) and a positive integer s,
find the shortest contiguous subarray which its sum is larger or equal to s.
If no such array exist, return 0. Otherwise return the length of subarray.

Args:
  minsum: int
  nums: list[int]
  logger: if given None, will use function's logger with DEBUG level

Return:
  length of shortest subarray which can sum to at least s

"""

import logging
import sys
import unittest

def minSubArrayLen2(minsum, nums, log=None):
    """
    O(N**2) solution: First build a prefix sum array for sums of subarray
    from 0 to current index, then use prefix sum array to calculate the sum
    of any subarray.
    """
    if log is None:
        log = logging.getLogger(sys._getframe().f_code.co_name)
        log.setLevel(logging.DEBUG)

    numslen = len(nums)
    prefix_sum = [0]
    curr_prefix_sum = 0
    for i in xrange(numslen):
        curr_prefix_sum += nums[i]
        prefix_sum.append(curr_prefix_sum)

    min_length = sys.maxint
    log.debug("Prefix sum list: " + str(prefix_sum))

    for i in xrange(1, numslen+1):
        for j in xrange(i+1):
            if prefix_sum[i] - prefix_sum[j] >= minsum:
                log.debug("Found subarray: starts index {0}, "
                          "ends index {1}, subarray: "
                          "{2}".format(j, i, str(nums[j:i+1])))
                min_length = min(min_length, i-j)
    if min_length == sys.maxint:
        return 0
    return min_length

def minSubArrayLen(minsum, nums, log=None):
    """
    O(N) solution: Use two pointers to track a subarray in current sliding
    window. Grow the window to right if sum of current window is smaller than
    minsum, shrink the window from left if sum is larger than minsum. This
    approach only need to scan the array in one pass.
    """
    if log is None:
        log = logging.getLogger(sys._getframe().f_code.co_name)
        log.setLevel(logging.DEBUG)

    left, right = 0, 1
    numslen = len(nums)
    prefix_sum = [0]
    curr_prefix_sum = 0
    for i in xrange(numslen):
        curr_prefix_sum += nums[i]
        prefix_sum.append(curr_prefix_sum)

    csum, min_length = 0, sys.maxint
    log.debug("Prefix sum list: " + str(prefix_sum))

    while right < numslen+1:
        log.debug("Current window: [{0}:{1}] :"
                  " {2}".format(left, right+1,
                                str(nums[left:right+1])))

        csum = prefix_sum[right] - prefix_sum[left]
        while left < right and csum >= minsum:
            min_length = min(min_length, right-left)
            left += 1
            csum = prefix_sum[right] - prefix_sum[left]
            log.debug("Growing window to: [{0}:{1}] :"
                      " {2}".format(left, right+1,
                                    str(nums[left:right+1])))

        if csum < minsum:
            right += 1
            log.debug("Shrinking window to: [{0}:{1}] :"
                      " {2}".format(left, right+1,
                                    str(nums[left:right+1])))

    if min_length == sys.maxint:
        return 0
    return min_length

class testShortestSubarray(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("ShortestSubarray")

    def test_1(self):
        print "Test 1"
        nums = [2,3,1,2,4,3]
        minsum = 7
        print "Input: {0}, {1}".format(str(nums), minsum)
        result2 = minSubArrayLen2(minsum, nums)
        print "Result:", result2
        assert result2 == 2
        result1 = minSubArrayLen(minsum, nums)
        print "Result:", result1
        assert result1 == 2
        print

    def test_2_null(self):
        print "Test 2: null input"
        nums = []
        minsum = 128
        print "Input: {0}, {1}".format(str(nums), minsum)
        result = minSubArrayLen(minsum, nums, self.logger)
        print "Result:", result
        assert result == 0
        print

    def test_3(self):
        print "Test 3"
        minsum = 213
        nums = [12,28,83,4,25,26,25,2,25,25,25,12]
        print "Input: {0}, {1}".format(str(nums), minsum)
        result = minSubArrayLen(minsum, nums, self.logger)
        print "Result:", result
        assert result == 8
        print

if __name__ == "__main__":
    unittest.main()
