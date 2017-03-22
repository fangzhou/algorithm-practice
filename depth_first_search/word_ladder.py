import logging
import sys
import unittest

"""
Problem: Given a dictionary, find a way to transform word A to word B.
All transformations can only modify one character in word, and all intermediate
words have to be in the dictionary.
"""


class DFSWordLadder:
    def __init__(self):
        self._dictionary = None
        self._visited = set()

    def onediff(self, str_a, str_b):
        """
        Check if 2 string only differs by one character
        """
        if len(str_a) != len(str_b):
            return False
        else:
            difflist = [0 if str_a[i] == str_b[i] else 1 for i in xrange(len(str_a))]
            if sum(difflist) == 1:
                return True
            else:
                return False

    def transform(self, word, endword, visited, jump):
        """
        Recursive transform beginning word to any word in dictionary
        """
        min_res = sys.maxint
        newstrs = []

        for j in self._dictionary:
            _od = self.onediff(word, j)
            if _od and j == endword:
                # Reached end
                return jump+1

            elif _od and j not in self._visited:
                # New word, unvisited
                self._visited.add(j)
                newstrs.append(j)
            else:
                continue

        for i in xrange(len(newstrs)):
            _r = self.transform(newstrs[i], endword, visited, jump+1)
            # Track the shortest transform path
            if _r < min_res:
                min_res = _r

        return min_res

    def ladderLength(self, S, E, D):
        """
        Args:
          S: start word
          E: end word
          D: dictionary
        """
        self._dictionary = D
        self._dictionary.add(E)
        self._visited.add(S)
        visited = []

        if len(S) != len(E):
            return 0
        if len(S) == 0:
            return 0
        self.L = len(S)

        return self.transform(S, E, visited, 1)

class TestWordLadder(unittest.TestCase):
    def setUp(self):
        self.DFSS = DFSWordLadder()

    def test_basic_0(self):
        print
        r = self.DFSS.ladderLength("a", "c", set(["a", "b", "c"]))
        print r

    def test_basic_1(self):
        print
        r = self.DFSS.ladderLength("hit", "cog", set(["hot", "dot", "dog", "lot", "log"]))
        print r

    def test_basic_2(self):
        print
        sword, eword = "qa", "sq"
        d = set(["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"])
        r = self.DFSS.ladderLength(sword, eword, d)
        print r


if __name__ == "__main__":
    unittest.main()
