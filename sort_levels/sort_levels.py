from collections import deque

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    if node is None:
        return []
    queue = deque([node])
    result = []
    while queue:
        root = queue.popleft()
        result.append(root.value)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
    return result