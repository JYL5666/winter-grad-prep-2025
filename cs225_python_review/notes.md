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

# Linked List Notes

## Definition
- Singly Linked List: nodes connected by next pointers.
- Each node stores: (value,next)
- Head points to first node; tail points to last node

## Core operations
- push_front(x): insert at head
- push_back(x): insert at tail 
- find(x): traverse until found
- traverse/ to_list(): walk through nodes

## Complexity
- Time:
  - push_front: O(1)
  - push_back: O(1) if we keep `tail`, otherwise O(n)
  - find / traverse: O(n)
- Space (extra space):
  - push_front/push_back/find: O(1)
  - to_list: O(n) (creates a Python list)
- Total storage: O(n) nodes

## Common pitfalls
- Forgetting to update `tail` when inserting into an empty list.
- missing `None` checks when traversing (cur becomes None).

# Stack / Queue (Python)

## Key points
- 1) Stack = LIFO. Core ops: push/pop/peek. Using Python list: append/pop are O(1) amortized.
- 2) Queue = FIFO. Core ops: enqueue/dequeue/peek. Using collections.deque: append/popleft are O(1).

## Program: stack_queue.py
### What the program does
- Implements Stack (list) and Queue (deque)
- Runs tests for normal case and empty-structure edge case

### Run log
#### Run 1 (normal)
Output:
All tests passed.

## Performance bottlenecks
- 1) list.pop(0) is O(n) because all elements shift left.
- 2) deque.popleft() is O(1), better for queue.

## Common pitfalls
- 1) Confusing LIFO (stack) and FIFO (queue)
- 2) Using list as a queue with pop(0) makes it slow for large n

# Hash Table

## Definition:
- A hash table stores (key, value). It uses hash(key) to map a key to an index in an array buckets.

## Ops:
- put(key, value): insert or update value for a key.
- get(key): return value for a key, raise key error if missing.
-uodate(key,value): same as put in my implementation.

## Complexity:
- Average: put/get O(1)
- Worst: O(n) if many keys collide into one bucket
- Space: O(n + m) where n = number of items, m = number of buckets