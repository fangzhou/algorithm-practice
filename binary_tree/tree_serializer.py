import math
import unittest

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    BFS base solution, will populate the full tree (including all leaves)
    """
    def serialize(self, root):
        """
        Encodes a tree to a comma separated string. Using level-order BFS.
        
        Args:
          root: TreeNode

        Return: serialized string
        """
        queue, result = [], []
        all_none = root is None
        next_all_none = False
        pop_count, last_pop_count = 0, 0
        queue.append(root)
        while not next_all_none:
            # Stop when next level is all none
            next_all_none = True
            pop_count = len(queue)
            last_pop_count = pop_count
            while pop_count > 0:
                _node = queue.pop(0)
                if _node is None:
                    queue.append(None)
                    queue.append(None)
                    result.append('None')
                else:
                    queue.append(_node.left)
                    queue.append(_node.right)
                    if _node.left is not None or _node.right is not None:
                        next_all_none = False
                    result.append(str(_node.val))
                pop_count -= 1
        return ','.join(result)

    def deserialize(self, data):
        """
        Decode serialized representation of a binary into a tree data structure.
        Since we serialized the full tree, we can implement this by calculating
        index.
        
        Args:
          data: str

        Return: TreeNode, root node
        """
        nodelist = [TreeNode(int(d)) if d != 'None' and len(d) > 0 else None
                    for d in data.split(',')]
        dlen = len(nodelist)

        if not math.log(dlen+1, 2).is_integer():
            raise AssertionError("Expect full serialized binary tree, "
                                 "please check if any null leaves are missing")

        # TODO: Automatically augment non-complete input
        
        numleaves = (dlen+1) / 2
        for i in xrange(dlen-numleaves):
            if nodelist[i] is not None:
                if i*2+1 < dlen:
                    nodelist[i].left = nodelist[i*2+1]
                if i*2+2 < dlen:
                    nodelist[i].right = nodelist[i*2+2]
        return nodelist[0]

class testBTCodec(unittest.TestCase):
    def setUp(self):
        self.btc = Codec()

    def test_1(self):
        print "Test 1:"
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        root.right.left.left = TreeNode(6)
        result = self.btc.serialize(root)
        print "Serialized result:", result

        dresult = self.btc.deserialize(result)
        print dresult.val
        print dresult.left.val
        print dresult.right.val
        print dresult.right.left.val
        print dresult.right.right.val
        print dresult.right.left.left.val

    def test_2(self):
        print "Test 2:"
        root = TreeNode(-1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        result = self.btc.serialize(root)
        print "Serialized result:", result

        dresult = self.btc.deserialize(result)
        print dresult.val
        print dresult.left.val
        print dresult.right.val

    def test_3(self):
        inputbuf = None
        with open('bigtest.txt', 'r') as testfile:
            inputbuf = testfile.readline()
        dresult = self.btc.deserialize(inputbuf)
        sresult = self.btc.serialize(dresult)
        print len(sresult), len(inputbuf)
        
if __name__ == "__main__":
    unittest.main()
