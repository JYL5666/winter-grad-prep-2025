from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, List

@dataclass
class Node:
    val: int
    next: Optional["Node"] = None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0
    
    def push_front(self, x: int) -> None:
        n = Node(x, self.head)
        self.head = n
        if self.tail is None:
            self.tail = n
        self.size += 1

    def push_back(self, x: int) -> None:
        n = Node(x, None)
        if self.tail is None:
            self.head = self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.size += 1
    def find(self, x: int) -> Optional[Node]:
        cur = self.head
        while cur is not None:
            if cur.val == x:
                return cur
            cur = cur.next
        return None
    def to_list(self) -> List[int]:
        out: List[int] = []
        cur = self.head
        while cur is not None:
            out.append(cur.val)
            cur = cur.next
        return out
    
if __name__ == "__main__":
    a = SinglyLinkedList()

    a.push_back(1)
    a.push_back(2)
    a.push_back(3)
    assert a.to_list() == [1,2,3]

    a.push_front(2)
    a.push_front(3)
    assert a.to_list() == [3,2,1,2,3]

    assert a.find(3) is not None and a.find(3).val == 3
    assert a.find(4) is None

    print("All test passed")

