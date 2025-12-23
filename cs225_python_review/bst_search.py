# __future__.annotations: Type annotations should be saved as text for now and not counted immediately (to avoid the trouble of self-referencing types)
# dataclass: Automatically generate boilerplate code for initialization, etc.
# Optional: Indicates "could be None" (BST child nodes are often empty)
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

# upper codes have same funtion with fellowing codes
#class Node:
#    def __init__(self.key):
#        self.key = key
#        self.left = None
#        self.right = None 

@dataclass
class Node:
    key: int
    left: Optional["Node"] = None
    right: Optional["Node"] = None

def insert(root: Optional[Node], key: int) -> Node:
    """Insert key into BST"""
    if root is None:
        return Node(key)
    
    cur = root
    while True:
        if key == cur.key:
            return root
        elif key < cur.key:
            if cur.left is None:
                cur.left =Node(key)
                return root
            cur = cur.left
        else:
            if cur.right is None:
                cur.right =Node(key)
                return root
            cur = cur.right

def search_iter(root: Optional[Node], key: int) -> Optional[Node]:
    """Iterative BST search."""
    cur = root
    while cur is not None:
        if key == cur.key:
            return cur
        elif key < cur.key:
            cur = cur.left
        else:
            cur = cur.right
    return None

def search_rec(root: Optional[Node], key: int) -> Optional[Node]:
    """Recursive BST search."""
    if root is None:
        return None
    if key == root.key:
        return root
    if key < root.key:
        return search_rec(root.left, key)
    return search_rec(root.right, key)

def _build_sample_tree() -> Node:
    keys = [7, 3, 10, 1, 14, 13]
    root: Optional[Node] = None
    for k in keys:
        root = insert(root,k)
    assert root is not None
    return root

if __name__ == "__main__":
    root = _build_sample_tree()
    # Test 1: found
    n = search_iter(root, 7)
    assert n is not None and n.key == 7
    # Test 2: not found
    n = search_iter(root, 5)
    assert n is None
    # Test 3 : recursive found
    n = search_rec(root, 3)
    assert n is not None and n.key == 3
    # Test 4 : empty tree
    assert search_iter(None, 1) is None
    print("All tests passed")