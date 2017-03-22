import logging
import random
import unittest

"""
Problem: Given an integer array, which is rotated from a sorted array, find
if a given value is in this array or not.
"""

class SearchRotate0(object):
    """
    Solution 1: First use binary search to find the turning point in the array,
    if the turning point is found, we can split the array into 2 sorted array
    and perform binary search in one of them.
    """

    def find_turn_point(self, nums, start, end):
        L = len(nums)
        mid = start + (end - start) / 2
        print start, mid, end, nums[start:end+1]
        if start == mid and mid == end:
            return start
        elif (end - start) == 1:
            if nums[start] > nums[end]:
                return start
            else:
                return end
        if nums[start] < nums[mid] and nums[mid] < nums[end]:
            # already sorted, no rotate
            return end
        elif nums[start] > nums[mid] and nums[mid] < nums[end]:
            # turning point is in first half (not including mid)
            return self.find_turn_point(nums, start, mid -1)
        elif nums[start] < nums[mid] and nums[mid] > nums[end]:
            # turning point is in second half (include mid)
            return self.find_turn_point(nums, mid, end)

    def binary_search(self, nums, t, start, end):
        L = len(nums)
        L2 = end - start + 1
        mid = start + (end - start) / 2
        print "\t", start, mid, end, t, nums[start:end]
        if (start == end) and (t != nums[start]):
            return -1
        elif nums[mid] == t:
            return mid
        elif t < nums[mid]:
            print "\t\tfront"
            return self.binary_search(nums, t, start, mid)
        elif t > nums[mid]:
            print "\t\tback"
            return self.binary_search(nums, t, mid+1, end)
        else:
            return -1

    def search(self, nums, target):
        """
        Args:
          nums: List[int]
          target: int

        Return: index of targer in nums
        """
        L = len(nums)
        tp = self.find_turn_point(nums, 0, L-1)
        print tp
        print nums[0:tp+1], nums[tp+1:], target
        if L == 1 and target != nums[0]:
            return -1
        if tp+1 >= L:
            return self.binary_search(nums, target, 0, L-1)
        elif nums[0] == target:
            return 0
        elif nums[tp] == target:
            return tp
        elif nums[L-1] == target:
            return L-1
        elif nums[0] <= target and target <= nums[tp]:
            return self.binary_search(nums, target, 0, tp)
        elif nums[tp+1] <= target and target <= nums[L-1]:
            return self.binary_search(nums, target, tp+1, L-1)


class SearchRotate(object):
    """
    Solution 2: Instead of finding turning point, we can use the relationship
    between the mid point and head and tail to search directly.
    """
    def search(self, nums, target):
        L = len(nums)
        head, tail = 0, L-1
        while head <= tail:
            mid = head + (tail - head) / 2
            if nums[mid] == target:
                # Direct hit
                return mid

            if mid == head:
                # Only 2 elements in search range
                if nums[head] == target:
                    return head
                elif nums[tail] == target:
                    return tail
                else:
                    return -1

            # Turning point can only be in front of mid point, or after it
            if nums[mid] < nums[tail]:
                # Turning point must be in front of mid
                if target > nums[mid] and target <= nums[tail]:
                    # Target falls between mid and tail, sorted second half
                    head, tail = mid+1, tail
                else:
                    # Target falls between head and mid, turning point in it
                    head, tail = head, mid-1
            elif nums[mid] > nums[head] and nums[head] > nums[tail]:
                # Turning point after mid
                if target >= nums[head] and target < nums[mid]:
                    # Target falls between head and mid, sorted first half
                    head, tail = head, mid-1
                else:
                    # Target falls between mid and tail, turning point in it
                    head, tail = mid+1, tail
        return -1

class testSearchRotate(unittest.TestCase):
    def setUp(self):
        self.S = SearchRotate()

    def generate_array(self):
        """
        Randomized test: Generate a random array, sort and rotate
        """

        L = random.randint(10, 16)
        p = random.randint(0, L)
        A = [random.randint(1, 200) for _ in xrange(L)]
        As = sorted(list(set(A)))
        Ar = As[p:] + As[:p]
        return Ar

    def _gold(self, A, t):
        """
        Brute force search to verify correctness of random testcase output
        """
        L = len(A)
        for i in xrange(L):
            if A[i] == t:
                return i
        return -1


    def test_1(self):
        A = [4,5,6,7,0,1,2]
        t = 6
        print "Test 1:\nInput: {0}, target: {1}".format(A, t)
        print self.S.search(A, t)

    def test_1_1(self):
        A = [1]
        t = 0
        print "Test 1.1: target not exist\nInput: {0}, target: {1}".format(A, t)
        print self.S.search(A, t)

    def test_1_2(self):
        A = [1]
        t = 2
        print "Test 1.2: target not exist\nInput: {0}, target: {1}".format(A, t)
        print self.S.search(A, t)

    def test_1_3(self):
        A = [1,3]
        t = 2
        print "Test 1.3: target not exist\nInput: {0}, target: {1}".format(A, t)
        print self.S.search(A, t)

    def test_1_4(self):
        A = [3,1]
        t = 1
        print "Test 1.4: two number in array (end of loop condition)\nInput: {0}, target: {1}".format(A, t)
        print self.S.search(A, t)

    def test_random(self):
        self.random_driver(1000)

    def random_driver(self, iters):
        import random
        passed_count = 0
        print "Running randomized tests..."
        for i in xrange(iters):
            # print
            A = self.generate_array()
            # print A
            t = A[random.randint(0, len(A)-1)]
            rc = self.S.search(A, t)
            rg = self._gold(A, t)
            if rc != rg:
                print "Error found:"
                print "  Array:", A, "\ttarget:", t
                print "  gold result:", rg, "\tactual result:", rc
            else:
                passed_count += 1
        print "Total passed cases: {0} out of total {1} cases".format(passed_count, iters)

if __name__ == "__main__":
    unittest.main()
