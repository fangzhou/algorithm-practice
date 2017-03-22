"""
Problem: Given a linked list which every node have an additional pointer,
points to another random node in the linked list. Write a function to deep
copy this linked list.
"""

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class DeepCopy(object):
    def copyRandomList(self, head):
        """
        First we build a reference map, key would be the label for each node 
        in the old linked list, and value is the new node corresponding to old
        node's random pointer. Then we scan through the list again to backfill
        the missing links.
        """
        refmap = dict()
        # Need this dummy node since we want to return the head of new list
        dummy = RandomListNode(-1)
        newlist_ptr = dummy
        oldlist_ptr = head
        
        while oldlist_ptr is not None:
            _new = RandomListNode(oldlist_ptr.label)
            if oldlist_ptr.random in refmap:
                # Old list's random pointer is already created for new list
                _new.random = refmap[oldlist_ptr.random]
            refmap[oldlist_ptr] = _new
            newlist_ptr.next = _new
            newlist_ptr = newlist_ptr.next
            oldlist_ptr = oldlist_ptr.next
            
        newlist_ptr = dummy.next
        oldlist_ptr = head

        # Second pass: for any missing random pointers, backfill using the
        # reference map
        while oldlist_ptr is not None:
            if newlist_ptr.random is None and oldlist_ptr.random is not None:
                newlist_ptr.random = refmap[oldlist_ptr.random]
            newlist_ptr = newlist_ptr.next
            oldlist_ptr = oldlist_ptr.next
        
        return dummy.next

