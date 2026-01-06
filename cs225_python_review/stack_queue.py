from collections import deque

class Stack:
    """LIFO stack using Python list."""
    def __init__(self):
        self._data = []
    
    def push(self, x):
        self._data.append(x)
    
    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()
    
    def peek(self):
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)

class Queue:
    """FIFO queue using collections.deque."""
    def __init__(self):
        self._data = deque()
    
    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.popleft()
    
    def peek(self):
        if not self._data:
            raise IndexError("peek from empty queue")
        return self._data[0]
    
    def is_empty(self):
        return len(self._data) == 0
    
    def __len__(self):
        return len(self._data)

def test_stack():
    s = Stack()
    s.push(10)
    s.push(20)
    assert len(s) == 2
    assert s.peek() == 20
    assert s.pop() == 20
    assert s.pop() == 10
    assert s.is_empty()

    try:
        s.pop()
    except IndexError:
        pass
    else:
        raise AssertionError("Expected IndexError for empty stack")
    
def test_queue():
    q = Queue()
    q.enqueue("a")
    q.enqueue("b")
    assert len(q) == 2
    assert q.peek() == "a"
    assert q.dequeue() == "a"
    assert q.dequeue() == "b"
    assert q.is_empty()

    try:
        q.dequeue()
    except IndexError:
        pass
    else:
        raise AssertionError("Expected IndexError for empty queue")
    
if __name__ == "__main__":
    test_stack()
    test_queue()
    print("All tests passed.")