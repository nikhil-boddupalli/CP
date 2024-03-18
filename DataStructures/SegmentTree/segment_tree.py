class Node():
    def __init__(self, start, end, val, left=None, right=None):
        self.start = start
        self.end = end
        self.val = val
        self.left = left
        self.right = right

# This instance keeps track of max element
# for each segment
class SegmentTree():    
    def query(self, root, query_start, query_end):
        start, end = root.start, root.end
        if query_end < start or query_start > end:
            return -int(1e9) # -ve infinity to maximum to be consistent
        if query_start <= start and query_end >= end:
            return root.val
        left_query = self.query(root.left, query_start, query_end)
        right_query = self.query(root.right, query_start, query_end)
        return max(left_query, right_query)

    def update(self, root, idx, val):
        start, end = root.start, root.end
        if start == idx:
            root.val = val
            return
        if end == idx:
            root.val = val
            return
        mid = (start + end) // 2
        if idx <= mid:
            self.update(root.left, start, mid)
        else:
            self.update(root.right, start, mid)
        
        root.val = max(root.left.val, root.right.max)


    def construct(self, arr, start, end):
        if start > end:
            return None
        if start == end:
            return Node(start, end, arr[start])
        mid = (start + end) // 2
        left_child = self.construct(arr, start, mid)
        right_child = self.construct(arr, mid+1, end)

        max_val = max(left_child.val, right_child.val)
        return Node(start, end, max_val, left_child, right_child)

