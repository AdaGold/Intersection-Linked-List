


from email.errors import HeaderParseError


class Node:
    def __init__(self, value):
        self.val = value
        self.next = None


def intersection_node(headA, headB):
    """ Will return the node at which the two lists intersect.
        --> pointing TO THE SAME REFERENCE IN MEMORY 
        If the two linked lists have no intersection at all, return None.
    """
# ''' create an empty variable to maintain the first seqential digit'''
    first = None
    current_a = headA
    current_b = headB
    
    while headA and headB:
# '''check to see if current_a is equal to current_b:'''
        if current_a is None and current_b is not None:
            current_a = headA
            current_b = current_b.next
        if current_b is None and current_a is not None:
            current_b = headB
            current_a = current_a.next
        while current_a != current_b:
            current_a = current_a.next
            current_b = current_b.next
            # return first
    # '''set the empty variable to first same node value'''
        if current_a == current_b:
            first = current_a
            return first

        elif current_a != current_b:
            return first
        else:
            return first

