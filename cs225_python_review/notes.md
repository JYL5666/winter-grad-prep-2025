# BST Search Notes

## Definition
- Binary Search Tree (BST): A data structure in computer science used for efficient searching, adding, and deleting data.
- BST property: left subtree keys < node.key < right subtree keys
- No duplicates (assume for this implementation)

## Core operations (how it search)
### Iterative search
- first, start at root
- if key == current.key: found
- else if key < current.key: go left
- else: go right
- Base case: If current becomes None: not found

### Recursive search
- same logic

## Complexity
- Time complexity: how long it runs
- Space compexity : how much extra memory it needs (usually excluding the input)
- Time: O(h), where h is tree height
  - Average: O(log n) if balanced (the tree is relatively "short and plump")
  - Worst: O(n) if skewed (the tree is very "tall and thin")
- Space:
  - Iterative: O(1)
  - Recursive: O(h) due to call stack
    Each time a function is called, the system saves a "stack frame" in the call stack. If you walk h levels along the tree, there will be approximately h simultaneous "pressing" calls on the stack